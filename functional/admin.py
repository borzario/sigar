from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

import keyboard
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
    await message.reply("what order you want to close? (Write number)")
    await OderClose.sost1.set()


async def close_oder(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["number"] = message.text
    await data_base.close_oder(message, data["number"])
    await state.finish()


class Giveto(StatesGroup):
    sost1 = State()
    sost2 = State()

async def start_give_order(message: types.Message):
    await message.reply("choose master from the list", reply_markup=keyboard.kbs_workers)
    await Giveto.sost1.set()


async def chose_master(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["master"] = list_of_admins.workers[f"{message.text}"]
    await message.reply("choose orders number")
    await Giveto.sost2.set()


async def chose_number(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["number"] = message.text
    await message.reply(f"order was send to worker")
    await data_base.send_order_to_master(state)
    await state.finish()


def registr_admin(dp: Dispatcher):
    dp.register_message_handler(start_close_call, lambda message: "Close call" in message.text, state=None)
    dp.register_message_handler(start_close_oder, lambda message: "Close order" in message.text, state=None)
    dp.register_message_handler(start_give_order, lambda message: "Give to" in message.text, state=None)
   # dp.register_message_handler(cancel, state="*", commands='отмена')
   # dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(close_call, state=CallClose.sost1)
    dp.register_message_handler(close_oder, state=OderClose.sost1)
    dp.register_message_handler(chose_master, state=Giveto.sost1)
    dp.register_message_handler(chose_number, state=Giveto.sost2)


