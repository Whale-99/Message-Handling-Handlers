import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '7750497362:AAG2BGu_yBVAHlXNPaeExhsFisisD4xdG2I'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

# Все остальные сообщения
@dp.message()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

# Запуск бота
if __name__ == '__main__':
    dp.run_polling(bot)
