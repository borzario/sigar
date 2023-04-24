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


class CallClose(StatesGroup):
    sost1 = State()


async def start_close_call(message: types.Message):
    await message.reply("what call you want to close? (Write number)")
    await CallClose.sost1.set()

async def close_call(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["number"] = message.text
    await data_base.close_call(message, data["number"])
    await state.finish()


def registr_admin(dp: Dispatcher):
    dp.register_message_handler(start_close_call, lambda message: "Close call" in message.text, state=None)
   # dp.register_message_handler(cancel, state="*", commands='отмена')
   # dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(close_call, state=CallClose.sost1)
