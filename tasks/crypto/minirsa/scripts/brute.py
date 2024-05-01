import gmpy2

n = 1170293403457

flag = 2
while n % flag != 0:
    flag = gmpy2.next_prime(flag)
    if n % flag == 0:
        print(flag, n // flag)