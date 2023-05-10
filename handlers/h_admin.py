from create_bot import *
from aiogram import types
import list_of_admins
import keyboard
import data_base


@dp.message_handler(lambda message: "admin" == message.text.lower())
async def choose_action(message: types.Message):
    if str(message.from_user.id) in list_of_admins.admins:
        await bot.send_message(message.from_user.id, "choose action, bro",
                               reply_markup=keyboard.kb_admin_main)


@dp.message_handler(lambda message: "get all calls" == message.text.lower())
async def get_all_calls(message: types.Message):
    if str(message.from_user.id) in list_of_admins.admins:
        await data_base.get_all_calls(message)
        await bot.send_message(message.from_user.id, "choose action, bro",
                               reply_markup=keyboard.kb_admin_main)


@dp.message_handler(lambda message: "get new calls" == message.text.lower())
async def get_new_call(message: types.Message):
    if str(message.from_user.id) in list_of_admins.admins:
        await data_base.get_new_calls(message)
        await bot.send_message(message.from_user.id, "choose action, bro",
                               reply_markup=keyboard.kb_admin_main)


@dp.message_handler(lambda message: "get all orders" == message.text.lower())
async def get_all_oders(message: types.Message):
    if str(message.from_user.id) in list_of_admins.admins:
        await data_base.get_all_oders(message)
        await bot.send_message(message.from_user.id, "choose action, bro",
                               reply_markup=keyboard.kb_admin_main)


@dp.message_handler(lambda message: "get new orders" == message.text.lower())
async def get_new_oders(message: types.Message):
    if str(message.from_user.id) in list_of_admins.admins:
        await data_base.get_new_oders(message)
        await bot.send_message(message.from_user.id, "choose action, bro",
                               reply_markup=keyboard.kb_admin_main)


@dp.message_handler(lambda message: message.text.lower() in ['accept', 'dislike'])
async def accept_order(message: types.Message):
    if str(message.from_user.id) in list_of_admins.workers_list:
        await data_base.accept_order(message)
        await message.reply("done")