from PIL import Image
import random


secret_string1 = b"mireactf{m1st3r_s3c_h1ded_s3cr3t}"
secret_string2 = b"hohoh_you_very_fanny_try_anotherr"

random_places = []
img = Image.open("mrPenisForCtf.jpg")
for i in range(500 - len(secret_string1), 500):
    random_places.append((random.randint(0, 1000), i))

for i in range(len(secret_string1)):
    img.putpixel(random_places[i], (secret_string1[i], img.getpixel(random_places[i])[1], img.getpixel(random_places[i])[2]))

img.save("bebebe1.png", bitmap_format="png")

img = Image.open("mrPenisForCtf.jpg")
for i in range(33):
    img.putpixel(random_places[i], (secret_string2[i], img.getpixel(random_places[i])[1], img.getpixel(random_places[i])[2]))

img.save("bebebe2.png", bitmap_format="png")
print(random_places)