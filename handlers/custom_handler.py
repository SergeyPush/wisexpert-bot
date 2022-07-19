from aiogram.types import InputFile

from config import bot, dp
from aiogram import types
from utils import back, kb_client, kb_inline
from utils import company_description, services_list, prices
from os import getcwd


@dp.message_handler()
async def get_about(message: types.Message):
    if message.text == "👸 Про нас":
        dir = getcwd()
        file = open(f"{dir}/static/image.png", "r+b")
        photo = InputFile(file)
        await message.answer_photo(photo)
        await bot.send_message(message.from_user.id, company_description)
    elif message.text == "💼 Послуги":
        await message.answer(services_list)
    elif message.text == "💵 Ціни":
        await message.answer(prices)
    elif message.text == "📞 Контакти":
        await message.answer("Наші контакти", reply_markup=kb_inline)


@dp.callback_query_handler(text=["open_instagram"])
async def get_contacts(call: types.CallbackQuery):
    await call.message.answer("https://www.instagram.com/wisexpert_buh/")


@dp.callback_query_handler(text=["open_facebook"])
async def get_contacts(call: types.CallbackQuery):
    await call.message.answer("https://www.facebook.com/WisExpert/")


@dp.callback_query_handler(text=["open_site"])
async def get_contacts(call: types.CallbackQuery):
    await call.message.answer("https://wisexpert.com.ua/")


@dp.callback_query_handler(text=["open_telegram"])
async def get_contacts(call: types.CallbackQuery):
    await call.message.answer("https://t.me/WisExpert")
