from dotenv import dotenv_values
from aiogram import Bot, Dispatcher, types

config = dotenv_values('.env')

bot = Bot(config["API_KEY"], parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
