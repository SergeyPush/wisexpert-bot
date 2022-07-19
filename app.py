from aiogram import executor
from utils.set_bot_commands import set_default_commands
from handlers import dp
from config import bot, API_KEY, HOST, ENV
import logging
import os

# webhook settings
WEBHOOK_HOST = HOST
WEBHOOK_PATH = f'/bot/{API_KEY}'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.environ.get('PORT', 5000))

logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    await set_default_commands(dp)
    await bot.set_webhook(WEBHOOK_URL)
    print("Bot started")


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    logging.warning('Bye!')


if __name__ == "__main__":
    print(f"Starting on {ENV}")
    if ENV == 'test':
        executor.start_polling(dp, skip_updates=True)
    if ENV == 'prod':
        executor.start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
        )
