from functools import wraps

from aiogram.types import Message, CallbackQuery
from loader import bot
from app.keyboards import user as keyboard


def debug_message_handler(func):
    @wraps(func)
    async def wrapper(message: Message, *args, **kwargs):
        try:
            await func(message, *args, **kwargs)
        except Exception as e:
            await message.answer(str(e), reply_markup=keyboard.main)

    return wrapper


def debug_callback_handler(func):
    @wraps(func)
    async def wrapper(callback_query: CallbackQuery, *args, **kwargs):
        try:
            await func(callback_query, *args, **kwargs)
        except Exception as e:
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=str(e), reply_markup=keyboard.main)

    return wrapper
