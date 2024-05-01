from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


products_button_text = "🛒 Товары"
profile_button_text = "ℹ️ Профиль"
replenishment_button_text = "💲 Пополнить баланс"
mainmenu_text = "🧋 Главное меню"
cancel_button_text = "Отменить"


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=products_button_text)],
    [KeyboardButton(text=profile_button_text)],
    [KeyboardButton(text=replenishment_button_text)]
], resize_keyboard=True)


cancel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=cancel_button_text)]
], resize_keyboard=True)


confirm_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Да', callback_data="confirm"),
     InlineKeyboardButton(text='Нет', callback_data="decline")]
])

