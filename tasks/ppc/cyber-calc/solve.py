from pwn import *
from sympy import simplify 
import decimal

HOST = '84.201.137.163'
PORT = 10214

r = remote(HOST, PORT)
count = 0
while True:
    data = r.recvline().decode()
    print(data)
    if "Solve: " in data:
        problem = data[7:data.index('[')] 
        solution = simplify(problem).evalf()
        solution = decimal.Decimal(str(solution))
        print(type(solution))
        print(problem, solution, count)
        r.sendline(str(solution).encode())
        count += 1
        if count == 999:
            data = r.recv().decode().strip()
            print(data)
            r.sendline(b"CyberCalc")
            data = r.recv().decode().strip()
            print(data)

    
