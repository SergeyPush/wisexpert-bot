from dotenv import dotenv_values
from aiogram import Bot, Dispatcher, types

config = dotenv_values('.env')
API_KEY = "5165676503:AAECCCPcYxUnTtRnzbhkrSukiwuUx-A3FqQ"
HOST = "https://orca-app-r6np6.ondigitalocean.app"

bot = Bot(API_KEY, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
