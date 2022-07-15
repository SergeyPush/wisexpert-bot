from aiogram import executor
from utils.set_bot_commands import set_default_commands
from handlers import dp


async def on_startup(_):
    await set_default_commands(dp)
    print("Bot started")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
