import base64
import csrandom

def xor(data, key):
    return bytes([d ^ k for d, k in zip(data, key * (len(data) // len(key) + 1))])

def generate_keystream(key):
    keystream = [71, 5, 73, 12, 134, 42, 97, 27, 157, 32, 81, 205, 143, 9, 44, 62]
    rnd = csrandom.Random(1337 - rnd_key)
    for i in range(len(keystream)):
        for j in range(keystream[i]):
            keystream[i] = rnd.Next(256)
    return keystream

yt_nick_cleartext  = b"H4xx0r"
yt_nick_ciphertext = base64.b64decode(b"fSAG0ldI")

yt_pass_cleartext  = b"rEzW7a6@KJy0n6K#z3"
yt_pass_ciphertext = base64.b64decode(b"ZiUjjg9uLosVNnLIek9BdjsE")

# The same can be done with service name
partial_keystream = xor(yt_nick_cleartext, yt_nick_ciphertext)

keystream_x_password = xor(yt_pass_cleartext, yt_pass_ciphertext)

partial_password = xor(keystream_x_password, partial_keystream)

rnd_key = int(partial_password[0])
keystream = generate_keystream(rnd_key)

password = xor(keystream_x_password, keystream)

print(password.decode())
