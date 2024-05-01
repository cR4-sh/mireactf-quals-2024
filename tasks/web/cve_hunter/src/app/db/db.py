import hashlib
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from app.db.cves_dict import cves_dict


load_dotenv()

ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
ADMIN_2FA = os.getenv('ADMIN_2FA')
SECRET_CODE = os.getenv('SECRET_CODE')


client = MongoClient('mongodb://localhost:27017/')
client.drop_database("CVEHunter")
db = client['CVEHunter']


def init():
    users = db.users
    cves = db.cves

    if not users.find_one({"username": "admin"}):
        add_user("admin", "admin@cvehunter.com", ADMIN_PASSWORD, ADMIN_2FA)

    if not users.find_one({"username": "guest"}):
        add_user("guest", "guest@cvehunter.com", "guest")

    for cve in cves_dict:
        if not cves.find_one({"cve_id": cve["cve_id"]}):
            cves.insert_one(cve)


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def add_user(username, email, password, password_2fa=None):
    hashed_password = hash_password(password)
    db.users.insert_one({
        "username": username,
        "email": email,
        "password": hashed_password,
        "password_2fa": password_2fa
    })


def authenticate_user(username, password):
    user = db.users.find_one({"username": username})
    if user and user['password'] == hash_password(password):
        return True, user
    return False, None


def verify_2fa(username, input_2fa_code):
    user = db.users.find_one({"$where": f"this.username == '{username}' && this.password_2fa == '{input_2fa_code}'"})
    return user


def get_all_cves():
    return list(db.cves.find({}, {"_id": 0, "cve_id": 1, "description": 1}))


def search_cve(cve_id):
    return db.cves.find_one({"cve_id": cve_id}, {"_id": 0})
