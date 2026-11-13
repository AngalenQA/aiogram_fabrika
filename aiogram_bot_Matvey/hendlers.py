from aiogram import Router, types
from aiogram.filters import Command
from keyboard.reply import main_kb
from keyboard.inline import get_confirm_kb
from aiogram import Router, F

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(text="Системы активированы. Выберите действие:", reply_markup=main_kb)

@router.message(F.text == "Мой профиль 👤")
async def profile(message: types.Message):
    await message.answer(text="Подтвердите запрос данных:", reply_markup=get_confirm_kb())