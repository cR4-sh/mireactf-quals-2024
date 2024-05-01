from PIL import Image

img1 = Image.open("bebebe1.png")
img2 = Image.open("bebebe2.png")

secret1 = ""
secret2 = ""

for i in range(img1.height):
    for j in range(img1.width):
        if img1.getpixel((j, i)) != img2.getpixel((j, i)):
            secret1 += chr(img1.getpixel((j, i))[0])
            secret2 += chr(img2.getpixel((j, i))[0])
            
print(secret2, " ", secret1)

