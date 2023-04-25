from create_bot import *
from aiogram import types
import list_of_admins
import keyboard


@dp.message_handler(lambda message: "start" in message.text.lower())
async def start(message: types.Message):
    if str(message.from_user.id) in list_of_admins.admins:
        await bot.send_message(message.from_user.id, "choose your status",
                               reply_markup=keyboard.kb_admin_first)
    else:
        await bot.send_message(message.from_user.id, "салам, ты кто будешь?",
                           reply_markup=keyboard.kb_firstwindow)
