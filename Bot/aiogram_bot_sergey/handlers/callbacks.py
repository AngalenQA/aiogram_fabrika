# --- ШАГ 1: Файл handlers/callbacks.py ---
from aiogram import Router, F, types


router = Router()


# Обрабатываем нажатие кнопки "confirm" из нашего модуля keyboards
@router.callback_query(F.data == "confirm")
async def process_confirm(callback: types.CallbackQuery):
    await callback.message.edit_text("✅ Запрос подтвержден. Доступ разрешен!")
    await callback.answer()


@router.callback_query(F.data == "cancel")
async def process_cancel(callback: types.CallbackQuery):
    await callback.message.edit_text("❌ Операция отменена Архитектором.")
    await callback.answer()