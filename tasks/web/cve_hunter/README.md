# web | Access Denied

## Information
 Твой товарищ по клавиатуре уверен, что сможет взломать E-Corp, если разживётся эксплойтом для CVE-2021-4034 с CVE Hunter. 
 Проблема в том, что доступ к эксплойтам – как в VIP-клуб - есть не у каждого.

## Writeup
Task solving via 2 stages
Flask unsign session cookie: brute secret key and sign evil session cookie.
To bypass 2fa - nosql injection. Flask debug is on, that simplify identify vulnerability. Work payload -  `' || ''=='`
And via access key get sploit cve-2021-4034 (flag)

## Flag
`mireactf{uuid}`