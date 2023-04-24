from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram.dispatcher.filters import Command
from aiogram.types.message import ContentType
import data_base
import keyboard
from create_bot import *
import data_base
import list_of_admins


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
async def close_call(message: types.Message):
    if str(message.from_user.id) in list_of_admins.admins:
        await data_base.get_new_calls(message)
        await bot.send_message(message.from_user.id, "choose action, bro",
                               reply_markup=keyboard.kb_admin_main)
