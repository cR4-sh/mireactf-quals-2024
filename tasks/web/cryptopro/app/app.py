from functools import wraps
import pickle
import random

from flask import Flask, jsonify, redirect, render_template, render_template_string, send_file, session, url_for, request, make_response

app = Flask(__name__)

encrypt_key = 'uiweiudwnhefiuwehfiuwefniwuefniuwefnwiuweojfoiwjefijwoifjwoifjowjfoiwjfijewfoijweoifjoiwjefojwfeiojwfoijwoifjwef'
secret_number = random.randint(10, 99)


class Wallet:
    def __init__(self):
        self.count = 0

    def load(self, data):
        self.__dict__ = pickle.loads(data)

    def save(self):
        return pickle.dumps(self.__dict__, 1)


balance = Wallet()


@app.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html", count=balance.count)


@app.route('/increment', methods=['POST'])
def increment():
    global balance
    balance.count += 1
    return jsonify({'count': balance.count})


@app.route('/save', methods=['POST', 'GET'])
def save():
    data = balance.save()
    data = data + int(secret_number).to_bytes(1, 'big')

    encrypt_key_bytes = encrypt_key.encode('utf-8')
    tmp = b""
    for i in range(len(data)):
        tmp += bytes([data[i] ^ encrypt_key_bytes[i % len(encrypt_key_bytes)]])
    data = tmp

    with open('wallet.bin', 'wb') as f:
        f.write(data)
    return send_file('wallet.bin', as_attachment=True)


@app.route('/load', methods=['POST', 'GET'])
def load():
    try:
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save('wallet.bin')
            with open('wallet.bin', 'rb') as f:
                data = f.read()

                encrypt_key_bytes = encrypt_key.encode('utf-8')

                tmp = b""
                for i in range(len(data)):
                    tmp += bytes([data[i] ^ encrypt_key_bytes[i %
                                    len(encrypt_key_bytes)]])
                balance_data = tmp[:-1]
                decrypted_secret_number_index = tmp[-1:]
                decrypted_secret_number = int.from_bytes(decrypted_secret_number_index, byteorder='big')

                if decrypted_secret_number != secret_number:
                    return render_template('index.html', error='The wallet is not signed by our service!')

                balance.load(balance_data)
    except Exception as e:
        return render_template('index.html', error=f'Something went wrong')

    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=False)
