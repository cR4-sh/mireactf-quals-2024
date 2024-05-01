from pwn import *
from ctypes import CDLL

if __name__ == '__main__':
    libc = CDLL("libc.so.6")

    for d in range(-10, 10):
        r = remote('84.201.137.163', 10290)
    
        now = int(math.floor(time.time())) + d
        libc.srand(now)
        
        for i in range(16):
            r.sendline(str(libc.rand() % 256).encode())
        r.recvuntil(b'Enter 16 numbers:')
        
        res = r.recvline(1)
        if b'mirea' in res:
            print(res)