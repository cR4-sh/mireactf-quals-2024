import decimal
import random
import re
import socket
import threading

from sympy import simplify
from img import print_calc


HOST = '0.0.0.0'
PORT = 12346

def establish_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print("Server started, waiting for connections...")
    return s

def generate_math_problem():
    operators = ['+', '-', '*', '/', '%']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    operator1 = random.choice(operators)
    operator2 = random.choice(operators)
    tmp = f"{random.choice(['', '('])}{random.choice([num1, num2, num3])}! {operator1} {random.choice([num1, num2, num3])}!"
    problem = f"{tmp}{f') {operator2}' if tmp[0] == '(' else f' {operator2}'} {random.choice([num1, num2, num3])}!"
    solution = simplify(problem).evalf()
    return problem, solution

def check_answer(answer, solution):
    epsilon = 1e-100
    threshold = 1
    if abs(answer - solution) < epsilon:
        return True
    elif abs(answer) > 0 or abs(solution) > 0:
        relative_difference = abs(answer - solution) / max(abs(answer), abs(solution))
        if relative_difference < threshold:
            return True
    return False


def handle_client(conn, addr):
    print(f"Connected by {addr}")

    conn.sendall(print_calc(0) + b"Welcome to the CyberCalc!\n" b"Show how good you are and solve these simple math problems! Good luck :)\n\n")
    try:

        for i in range(1000):
            if i == 999:
                conn.sendall(b"You've almost done it, but I have one last question. What is the name of the task?")
                data = conn.recv(1024).decode().strip()
                if str(data) == 'CyberCalc':
                    conn.sendall(b"Congratulations! You've completed all problems.\n" + 
                    print_calc(2))
                    conn.close()
                else:
                    conn.sendall(b"Incorrect! Bye bye!\n" + print_calc(1))
                    conn.close()
                    break

            problem, solution = generate_math_problem()
        
            conn.sendall(f"Solve: {problem} [{i}/1000]\n".encode() )
            data = conn.recv(1024).decode().strip()
            try:
                regex = r'^-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?$'
                if re.match(regex, data):
                    try:
                        answer = simplify(data).evalf()
                        if check_answer(answer=answer, solution=solution):
                            conn.sendall(b"Correct!\n")
                        else:
                            conn.sendall(b"Incorrect! Bye bye!\n" + print_calc(1))
                            conn.close()
                    except:
                        conn.sendall(b"Incorrect! Bye bye!\n" + print_calc(1))
                        conn.close()
                    
                else:
                    conn.sendall(b"Incorrect! Bye bye!\n" + print_calc(1))
                    conn.close()
            except decimal.InvalidOperation:
                conn.sendall(b"Invalid input! Try again.\n" + print_calc(1))
                break
            except BrokenPipeError:
                print("Connection closed by client.")
                break
        conn.close()
    
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        conn.close()   


def main():
    s = establish_connection()
    while True:
        try:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
        except ConnectionResetError:
            print("ConnectionResetError occurred. Re-establishing connection.")
        except KeyboardInterrupt:
            print("Server is shutting down...")
            break
    s.close()         

if __name__ == "__main__":
    main()
            