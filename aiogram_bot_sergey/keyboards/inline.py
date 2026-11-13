from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def get_confirm_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Подтвердить ✅", callback_data="confirm"))
    builder.add(InlineKeyboardButton(text="Отмена ❌", callback_data="cancel"))
    return builder.as_markup()