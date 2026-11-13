from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Мой профиль 👤")],
        [KeyboardButton(text="Начать квест ⚔️")]
    ],
    resize_keyboard=True
)