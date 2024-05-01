from flask import Flask, request, jsonify, session, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import random
import os
import string


app = Flask(__name__)
app.secret_key = 'g8y348f3h4f34jf93ij4g3u49gh343kdawec3jj3kgg43kx4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:5432/slickytips'
counter = 0
db = SQLAlchemy(app)
Base = declarative_base()
FLAG = os.getenv('FLAG', 'flag{fakeflag}')


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    tips = Column(String)
    main_tip = Column(String)


@app.route("/api/register", methods=["POST"])
def reg():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    exist_user = User.query.filter_by(username=username).first()

    if exist_user:
        return jsonify({"message":"User already exist"}), 400
    
    new_user = User(username=username,password=password, tips=generate_tips(), main_tip=generate_main_tip())
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message":"User created successful"})
        

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user:
        stored_pass = user.password.encode('utf-8')
        input_pass = password.encode('utf-8')
        if stored_pass == input_pass:
            session['user'] = username
            return jsonify({"message":"Login Successful"})
        else:
            return jsonify({"message":"Incorrect password"}), 401
    return jsonify({"message":"User not found"}), 404


@app.route("/api/user", methods=["GET"])
def userinfo():
    if 'user' in session:
        username = session['user']
        user = User.query.filter_by(username=username).first()
        if user:
            user_info = {
                'tips':user.tips+user.main_tip,
                'username':user.username,
                'id':user.id
            }
            return jsonify(user_info)
        else:
            return jsonify({'message':'User not found'}), 404
    else:
        return jsonify({'message':'Unathorized'}), 401
    

@app.get('/')
def index():
    return redirect("/login", 302)

@app.get('/login')
def login_handler():
    return render_template('login.html')

@app.get('/info')
def info():
    return render_template('info.html')

@app.route('/submit', methods=['POST','GET'])
def submit():
    global counter
    if request.method == 'GET':
        if counter >= 100:
            return render_template('submit.html', flag=FLAG)
        else:
            return render_template('submit.html', remain=100-counter)
    
    data = request.get_json()
    part_flag = data['flag']
    exist = User.query.filter(User.main_tip == part_flag).count()
    usr = User.query.filter(User.main_tip == part_flag).first()

    if exist != 0:
        usr.main_tip = "Expired"
        db.session.commit()
        counter += 1
        return jsonify({"message":"Success submit"})
    return jsonify({"message":"Invalid flag"}), 400


def generate_tips():
    with open('tips.txt','r') as file:
        all_tips = file.readlines()
    for i in all_tips:
        i = i.replace('\n','')
    tips = all_tips[random.randint(0,len(all_tips)-1)] + all_tips[random.randint(0,len(all_tips))-1] + all_tips[random.randint(0,len(all_tips)-1)]
    return tips


def generate_main_tip():
    characters = string.ascii_uppercase + string.digits
    generated_string = ''.join(random.choice(characters) for _ in range(31))
    return f"{generated_string}="


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)