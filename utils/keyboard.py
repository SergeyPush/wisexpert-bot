from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

about = KeyboardButton('👸 Про нас')
services = KeyboardButton('💼 Послуги')
prices = KeyboardButton('💵 Ціни')
contacts = KeyboardButton('📞 Контакти')
back_button = KeyboardButton("Return")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(about, services)
kb_client.row(prices, contacts)

back = ReplyKeyboardMarkup(resize_keyboard=True)
back.insert(back_button)

instagram_inline_button = InlineKeyboardButton(text="Instagram", callback_data="open_instagram",
                                               url="https://www.instagram.com/wisexpert_buh/")
facebook_inline_button = InlineKeyboardButton(text="Facebook", callback_data="open_facebook",
                                              url="https://www.facebook.com/WisExpert/")
site_inline_button = InlineKeyboardButton(text="Website", callback_data="open_site", url="https://wisexpert.com.ua/")
contacts_inline_button = InlineKeyboardButton(text="Telegram", callback_data="open_telegram",
                                              url="https://t.me/WisExpert")

kb_inline = InlineKeyboardMarkup()
kb_inline.row(instagram_inline_button, facebook_inline_button)
kb_inline.row(site_inline_button, contacts_inline_button)
