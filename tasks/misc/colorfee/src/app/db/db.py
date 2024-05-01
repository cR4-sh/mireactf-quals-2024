import os
import asyncpg

from dotenv import load_dotenv


load_dotenv()


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_HOST = os.getenv("DB_HOST")
FLAG = os.getenv("FLAG")


class Coffee:
    def __init__(self):
        self.db_pool = None

    async def setup(self):
        self.db_pool = await asyncpg.create_pool(
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE,
            host=DB_HOST
        )
        await self.create_tables()
        await self.populate_products()

    async def create_tables(self):
        async with self.db_pool.acquire() as conn:
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                    user_id BIGINT PRIMARY KEY,
                    balance INTEGER NOT NULL DEFAULT 0,
                    last_purchase TEXT
                );
            ''')
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS Products (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE,
                    price INTEGER NOT NULL,
                    purchase_text TEXT NOT NULL
                );
            ''')
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS Orders (
                    id SERIAL PRIMARY KEY,
                    user_id BIGINT REFERENCES Users(user_id),
                    product_id INTEGER REFERENCES Products(id),
                    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
                );
            ''')

    async def populate_products(self):
        products = [
            ("🍊 Цитрусовый Раф", 0, "Спасибо за покупку 🍊 Цитрусовый Раф! Можете забрать свой заказ на кассе. Промокод на следующий заказ: RAF_coupon_20 — работает только на оффлайн заказы через кассу."),
            ("🟢 Матча Латтеато", 150, "Спасибо за покупку 🟢 Матча Латтеато! Можете забрать свой заказ на кассе. Промокод на следующий заказ: Latte_coupon_30 — работает только на оффлайн заказы через кассу."),
            ("🍓 Клубничный Эликсир", 200, "Спасибо за покупку 🍓 Клубничный Эликсир! Можете забрать свой заказ на кассе. Промокод на следующий заказ: Stawberry_coupon_40 — работает только на оффлайн заказы через кассу."),
            ("🦋 <b>ХИТ: Голубинный Оазис</b>", 1337, FLAG)
        ]
        async with self.db_pool.acquire() as conn:
            for name, price, purchase_text in products:
                await conn.execute(f'''
                    INSERT INTO Products (name, price, purchase_text)
                    VALUES ('{name}', {price}, '{purchase_text}')
                    ON CONFLICT (name) DO NOTHING;
                ''')

    async def add_new_user(self, user_id):
        async with self.db_pool.acquire() as conn:
            await conn.execute(f'''
                INSERT INTO Users (user_id) VALUES ({user_id})
                ON CONFLICT (user_id) DO NOTHING;
            ''')

    async def get_user_balance(self, user_id):
        async with self.db_pool.acquire() as conn:
            return await conn.fetchval(f'''
                SELECT balance FROM Users WHERE user_id = {user_id};
            ''')

    async def get_user_last_purchase(self, user_id):
        async with self.db_pool.acquire() as conn:
            return await conn.fetchval(f'''
                SELECT last_purchase FROM Users WHERE user_id = {user_id};
            ''')

    async def get_products(self):
        async with self.db_pool.acquire() as conn:
            products = await conn.fetch(f'''
                    SELECT id, name, price FROM products;
                ''')
            if products:
                return products
            else:
                return "Товары закончились"

    async def make_purchase(self, user_id, product_id):
        async with self.db_pool.acquire() as conn:
            price_query = f"SELECT price FROM Products WHERE id = {product_id};"
            price = await conn.fetchval(price_query)

            if price is None:
                return f"Товар не найден"

            balance_query = f"SELECT balance FROM Users WHERE user_id = {user_id};"
            balance = await conn.fetchval(balance_query)

            if balance >= price:
                purchase_text_query = f"SELECT purchase_text FROM Products WHERE id = {product_id};"
                purchase_text = await conn.fetchval(purchase_text_query)

                new_balance = balance - price

                update_query = f"UPDATE Users SET balance = {new_balance}, last_purchase = '{purchase_text}' WHERE user_id = {user_id};"
                await conn.execute(update_query)

                return purchase_text
            else:
                return "Недостаточно средств"

