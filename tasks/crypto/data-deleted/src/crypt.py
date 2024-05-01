key  =   "ТИПЬЕФГЮВЯНЭКЦДЖЪОХСЁШЩРЫЧЗЛБМУАЙ"
alpha =  "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
d = {}
for i in range(len(key)):
    d.update([(alpha[i], key[i])])
    d.update([(alpha[i].lower(), key[i].lower())])

with open("ciphertext.txt", "w") as f:
    with open("decryptedtext.txt") as c:
        for i in c.read():
            if i in d:
                f.write(d[i])
            else:
                f.write(i)