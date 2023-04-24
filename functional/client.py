from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram.dispatcher.filters import Command
from aiogram.types.message import ContentType
import data_base


class CallOrder(StatesGroup):
    sost1 = State()
    sost2 = State()
    sost3 = State()
    sost4 = State()

async def start_order_call(message: types.Message):
    await message.reply("Как к тебе обращаться, черт?")
    await CallOrder.sost1.set()

async def get_name(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await message.reply("Куда тебе шуметь")
    await CallOrder.sost2.set()

async def get_contact(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["contact"] = message.text
    await message.reply("when?")
    await CallOrder.sost3.set()

async def get_time(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["time"] = message.text
    await message.reply("Готово, ходи и оглядывайся")
    await data_base.add_call_to_user(state)
    await state.finish()


def registr_client(dp: Dispatcher):
    dp.register_message_handler(start_order_call, lambda message: "Заказать звонок" in message.text, state=None)
   # dp.register_message_handler(cancel, state="*", commands='отмена')
   # dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(get_name, state=CallOrder.sost1)
    dp.register_message_handler(get_contact, state=CallOrder.sost2)
    dp.register_message_handler(get_time, state=CallOrder.sost3)




