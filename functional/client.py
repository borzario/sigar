from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
import data_base
import keyboard


class CallOrder(StatesGroup):
    sost1 = State()
    sost2 = State()
    sost3 = State()
    sost4 = State()

async def start_order_call(message: types.Message):
    await message.reply("Как к тебе обращаться, черт?", reply_markup=keyboard.kb_cancel)
    await CallOrder.sost1.set()

async def cancel(message : types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK", reply_markup=keyboard.kb_mainwindow)

async def get_name(message : types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await message.reply("Куда тебе шуметь", reply_markup=keyboard.kb_cancel)
    await CallOrder.sost2.set()

async def get_contact(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["contact"] = message.text
    await message.reply("when?", reply_markup=keyboard.kb_cancel)
    await CallOrder.sost3.set()

async def get_time(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["time"] = message.text
    await message.reply("Готово, ходи и оглядывайся", reply_markup=keyboard.ib_main)
    await data_base.add_call_to_user(state)
    await state.finish()


class MasterCall(StatesGroup):
    sost1 = State()
    sost2 = State()
    sost3 = State()
    sost4 = State()
    sost5 = State()

async def start_master_call(message: types.Message):
    await message.reply("Как к тебе обращаться, черт?", reply_markup=keyboard.kb_cancel)
    await MasterCall.sost1.set()


async def get_name_for_master(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await message.reply("Куда тебе шуметь", reply_markup=keyboard.kb_cancel)
    await MasterCall.sost2.set()


async def get_contact_for_master(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["contact"] = message.text
    await message.reply("when?", reply_markup=keyboard.kb_cancel)
    await MasterCall.sost3.set()


async def get_time_master(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["time"] = message.text
    await message.reply("what service? tap on keyboard", reply_markup=keyboard.kb_servises)
    await MasterCall.sost4.set()

async def get_service_info(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["service"] = message.text
        data["type"] = await data_base.get_info_about_user(message)
    await message.reply("write about your problem", reply_markup=keyboard.kb_cancel)
    await MasterCall.sost5.set()

async def get_discription(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["discription"] = message.text
    await message.reply("Готово, ходи и оглядывайся", reply_markup=keyboard.ib_main)
    await data_base.add_master_call(state)
    await state.finish()


def registr_client(dp: Dispatcher):
    dp.register_message_handler(start_order_call, lambda message: "Заказать звонок" in message.text, state=None)
    dp.register_message_handler(start_master_call, lambda message: "Вызов мастера" in message.text, state=None)
    dp.register_message_handler(cancel, state="*", commands='отмена')
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(get_name, state=CallOrder.sost1)
    dp.register_message_handler(get_contact, state=CallOrder.sost2)
    dp.register_message_handler(get_time, state=CallOrder.sost3)
    dp.register_message_handler(get_name_for_master, state=MasterCall.sost1)
    dp.register_message_handler(get_contact_for_master, state=MasterCall.sost2)
    dp.register_message_handler(get_time_master, state=MasterCall.sost3)
    dp.register_message_handler(get_service_info, state=MasterCall.sost4)
    dp.register_message_handler(get_discription, state=MasterCall.sost5)




