import random
import os


key = random.randbytes(8)

im = open("NahIdXorCtf.png", "rb")

with open("NahCrypted.png", "wb") as f:
    for i in range(os.path.getsize("NahIdXorCtf.png")):
        f.write((im.read(1)[0] ^ key[i%8]).to_bytes(1, "big"))

print(key)