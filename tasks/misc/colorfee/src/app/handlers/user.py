from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from app.keyboards import user as keyboard
from app.utils.debug import debug_message_handler, debug_callback_handler
from app.utils.states import BuyForm
from loader import bot, db

router = Router()

start_photo_id = "AgACAgIAAxkBAANPZderBzAy2deITswzveoVkRD-fz8AAoHUMRsAAUrBSrc4wYIPmxTAAQADAgADeQADNAQ"
products_photo_id = "AgACAgIAAxkBAANSZderGfEQh2ITg_pd4iFT1_8tU7QAAoLUMRsAAUrBSk9pUK99eRc6AQADAgADeQADNAQ"


# Команда /start
@router.message(CommandStart())
@debug_message_handler
async def start(message: Message, state: FSMContext):
    await state.clear()
    await db.add_new_user(message.from_user.id)
    text = "Добро пожаловать в магазин с удивительным" \
           " ассортиментом кофе! Здесь вы можете приобрести" \
           " различные кофейные напитки на любой вкус и цВеТ☕️"

    await message.answer_photo(photo=start_photo_id, caption=text,
                               reply_markup=keyboard.main)


# Кнопка Отменить
@router.message(F.text == keyboard.cancel_button_text)
@debug_message_handler
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(keyboard.mainmenu_text, reply_markup=keyboard.main)


# Кнопка 🛒 Товары
@router.message(F.text == keyboard.products_button_text)
@debug_message_handler
async def products(message: Message, state: FSMContext):
    await state.set_state(BuyForm.position)

    products_items = await db.get_products()
    if products_items == "Товары закончились":
        await message.answer("Извините, но товары временно закончились.")
        return

    text = "Только сегодня! В честь открытия кофейни мы готовим всем желающим бесплатный Цитрусовый Раф 🍊💥\n\n" \
           "Актуальное меню:\n" \
           "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"

    for index, product in enumerate(products_items, start=1):
        text += f"{index}. {product['name']} | {product['price']}₽\n"

    text += "➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nВведите номер позиции, которую хотите заказать"

    await message.answer_photo(photo=products_photo_id, caption=text,
                               reply_markup=keyboard.cancel,
                               parse_mode=ParseMode.HTML)


# Подтверждение покупки
@router.message(BuyForm.position)
@debug_message_handler
async def confirm_buy(message: Message, state: FSMContext):
    await state.clear()
    await state.update_data(position=message.text)
    await message.answer("Вы уверены что хотите приобрести этот напиток?",
                         reply_markup=keyboard.confirm_ikb)
    await state.set_state(BuyForm.confirm)


# Кнопка Да и Нет при подтверждении покупки
@router.callback_query()
@debug_callback_handler
async def purchase(callback_query: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    if await state.get_state() != BuyForm.confirm:
        return

    if callback_query.data == 'confirm':
        product_id = (await state.get_data())["position"]
        text = await db.make_purchase(callback_query.from_user.id, product_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=text, reply_markup=keyboard.main)
    else:
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=keyboard.mainmenu_text,
                               reply_markup=keyboard.main)
    await state.clear()


# Кнопка ℹ️ Профиль
@router.message(F.text == keyboard.profile_button_text)
@debug_message_handler
async def profile_info(message: Message):
    text = f"➖➖➖➖➖➖➖➖➖➖➖\nℹ️ Информация о вас:\n"
    if message.from_user.username:
        text += f"🔑 Логин: {message.from_user.username}\n"

    user_balance = await db.get_user_balance(message.from_user.id)
    text += f"💳 ID: {message.from_user.id}\n\n" \
            f"🏦 Баланс: {user_balance} руб.\n➖➖➖➖➖➖➖➖➖➖➖"

    user_last_purchase = await db.get_user_last_purchase(message.from_user.id)
    if user_last_purchase:
        text += f"\nВаша последняя покупка:\n{user_last_purchase}"

    await message.answer(text=text, reply_markup=keyboard.main)


# Кнопка 💲 Пополнить баланс
@router.message(F.text == keyboard.replenishment_button_text)
@debug_message_handler
async def profile_info(message: Message):
    await message.answer("К сожалению, оплата сломана и будет"
                         " отремонтирована только в 2077 веке. Приносим"
                         " извинения за неудобства :(",
                         reply_markup=keyboard.main)


# Любое сообщение не попавшее в другие хэндлеры
@router.message()
@debug_message_handler
async def any_message(message: Message, state: FSMContext):
    await state.clear()
    await db.add_new_user(message.from_user.id)
    text = "Добро пожаловать в магазин с удивительным" \
           " ассортиментом кофе! Здесь вы можете приобрести" \
           " различные кофейные напитки на любой вкус и цВеТ☕️"

    await message.answer_photo(photo=start_photo_id, caption=text,
                               reply_markup=keyboard.main)

