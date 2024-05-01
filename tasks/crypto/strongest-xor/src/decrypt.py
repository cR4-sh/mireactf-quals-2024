import os

png_signatre = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
print(png_signatre)
with open("NahCrypted.png", "rb") as f:
    key = bytes(a ^ b for a, b in zip(f.read(8), png_signatre))
print(key)

im = open("NahCrypted.png", "rb")

with open("NahDecrypted.png", "wb") as f:
    for i in range(os.path.getsize("NahCrypted.png")):
        f.write((im.read(1)[0] ^ key[i%8]).to_bytes(1, "big"))

