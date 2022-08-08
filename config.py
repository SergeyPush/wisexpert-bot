from dotenv import dotenv_values, load_dotenv
from aiogram import Bot, Dispatcher, types
from os import environ as env

load_dotenv()
HOST = env.get('WEBHOOK_HOST')
ENV = env.get('ENV', default='dev')
API_KEY = env.get('API_KEY')

bot = Bot(API_KEY, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
