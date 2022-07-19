from dotenv import dotenv_values, load_dotenv
from aiogram import Bot, Dispatcher, types
from os import environ as env

load_dotenv()
HOST = "https://orca-app-r6np6.ondigitalocean.app"
ENV = env.get('ENV')
API_KEY = env.get('API_KEY')

bot = Bot(API_KEY, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
