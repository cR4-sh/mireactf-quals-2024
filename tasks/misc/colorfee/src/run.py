import asyncio
import logging
import aioredis

from aiogram import Dispatcher

from loader import bot, db
from app.utils.middlewares import AntiFloodMiddleware
from app.handlers.user import router


async def main():
    dp = Dispatcher()

    router.message.middleware(AntiFloodMiddleware())

    dp.include_router(router)

    await db.setup()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Pressed Ctrl + C.")
