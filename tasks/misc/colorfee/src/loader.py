import os

from dotenv import load_dotenv
from aiogram import Bot
from app.db.db import Coffee


load_dotenv()

db = Coffee()
bot = Bot(token=os.environ.get('BOT_TOKEN'))
