from dotenv import dotenv_values
from aiogram import Bot, Dispatcher, types

config = dotenv_values('.env')
API_KEY = "5165676503:AAEHXEpgmRPzzSAxYpz_Tysr5v6P985mBD4"
HOST = "https://git.heroku.com/wisexpert-bot.git"

bot = Bot(API_KEY, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
