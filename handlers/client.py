from config import bot, dp
from aiogram import types
from utils import kb_client


@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Бухгалтерська компанія WisExpert. Оберіть що Вас цікавить",
                           reply_markup=kb_client)

# @dp.message_handler(commands=["about"])
# async def command_start(message: types.Message):
#     await message.answer("This is description of our <b>amazing</b> company")


# @dp.message_handler(commands=["help"])
# async def command_start(message: types.Message):
#     await bot.send_message(message.from_user.id, "Get help")
