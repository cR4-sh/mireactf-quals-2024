import gmpy2
import os

flag = b"mireactf{y0u_n33d_larg3r_numb3rs}"
remainder = len(flag) % 5

if remainder:
    flag += b'\x00' * (5 - remainder)

flag = [int.from_bytes(flag[i - 5:i]) for i in range(5, len(flag) + 1, 5)]

e = 11

p = 1081789
q = 1081813
N = p*q

phi_n = (p - 1) * (q - 1)


def crypt(text: list, e: int, n: int) -> bytes:
    encrypted_int = [pow(i, e, n) for i in text]

    return encrypted_int

def decrypt(ciphertext: list, d: int, n: int) -> bytes:
    decrypted_int = [int(pow(i, d, n)).to_bytes(5, "big") for i in ciphertext]

    return decrypted_int
    

def calculate_d(p, q, e):
    phi_n = (p - 1) * (q - 1)
    d = gmpy2.invert(e, phi_n)
    return d

print(N)
print(e)
c = crypt(flag, e, N)
print(c)
print((decrypt(c, calculate_d(p, q, e), N)))