from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from create_bot import *
import data_base
import list_of_admins


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


class OderClose(StatesGroup):
    sost1 = State()


async def start_close_oder(message: types.Message):
    await message.reply("what oder you want to close? (Write number)")
    await OderClose.sost1.set()

async def close_oder(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["number"] = message.text
    await data_base.close_oder(message, data["number"])
    await state.finish()


def registr_admin(dp: Dispatcher):
    dp.register_message_handler(start_close_call, lambda message: "Close call" in message.text, state=None)
    dp.register_message_handler(start_close_oder, lambda message: "Close oder" in message.text, state=None)
   # dp.register_message_handler(cancel, state="*", commands='отмена')
   # dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(close_call, state=CallClose.sost1)
    dp.register_message_handler(close_oder, state=OderClose.sost1)

