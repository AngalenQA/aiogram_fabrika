from aiogram import Router, types
from aiogram.filters import Command

# ИМПОРТ: Достаем делали со шкафа
from keyboards.reply import main_kb
from keyboards.inline import get_confirm_kb
from aiogram import Router, F


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Система активна. Выберите действие:", reply_markup=main_kb)


@router.message(F.text == "Мой профиль 👤")
async def show_profile(message: types.Message):
    await message.answer("Подтвердите запрос данных:", reply_markup=get_confirm_kb())