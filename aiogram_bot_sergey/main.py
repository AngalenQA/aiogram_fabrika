import asyncio
from aiogram import Bot, Dispatcher
from handlers import router as main_router # Импорт нашего роутера
from handlers import callbacks
async def main():
    bot = Bot(token="ТВОЙ_ТОКЕН")
    dp = Dispatcher()


    # Подключаем роутер к главному диспетчеру
    dp.include_router(callbacks.router)
    dp.include_router(main_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())