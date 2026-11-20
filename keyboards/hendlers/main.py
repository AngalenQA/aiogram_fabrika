import asyncio
from aiogram import Bot, Dispatcher
from keyboards.hendlers import router as main_router # Импорт нашего роутера
from keyboards.hendlers import callbacks
async def main():
    bot = Bot(token="8969930711:AAELw20NLzTHxZ3fupj573K2_c_opV1yYDE")
    dp = Dispatcher()


    # Подключаем роутер к главному диспетчеру
    dp.include_router(callbacks.router)
    dp.include_router(main_router)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())