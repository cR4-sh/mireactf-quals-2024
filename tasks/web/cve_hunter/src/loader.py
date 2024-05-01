from dotenv import load_dotenv
from app.db import db
import os


load_dotenv()
db.init()

SECRET_CODE = os.getenv('SECRET_CODE')
FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
