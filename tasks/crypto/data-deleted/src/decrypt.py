key  =  "ТИПЬЕФГЮВЯНЭКЦДЖЪОХСЁШЩРЫЧЗЛБМУАЙ"
alpha = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

d = {}
for i in range(len(key)):
    d.update([(key[i], alpha[i])])
    d.update([(key[i].lower(), alpha[i].lower())])

with open("decryptedtext.txt", "w") as f:
    with open("ciphertext.txt") as c:
        for i in c.read():
            if i in d:
                f.write(d[i])
            else:
                f.write(i)