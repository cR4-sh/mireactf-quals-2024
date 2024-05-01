from aiogram.fsm.state import StatesGroup, State


class BuyForm(StatesGroup):
    position = State()
    confirm = State()
