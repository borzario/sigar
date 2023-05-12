from create_bot import *
from aiogram import types
import keyboard
import data_base

@dp.message_handler(lambda message: message.text.lower() in ["частное лицо", "компания"])
async def go_to_main_fromstart(message: types.Message):
    await bot.send_message(message.from_user.id, "Приветствуем Вас!",
                           reply_markup=keyboard.kb_mainwindow)
    await data_base.user_add(message)


@dp.callback_query_handler(text="в начало")
@dp.message_handler(lambda message: message.text.lower() in ["user", "/main"])
async def go_to_main(message: types.Message):
       await bot.send_message(message.from_user.id, "Приветствуем Вас!",
                               reply_markup=keyboard.kb_mainwindow)


@dp.message_handler(lambda message: "адрес компании" in message.text.lower())
async def push_adress(message: types.Message):
    await bot.send_message(message.from_user.id, "г. Томск, ул. Большая Подгорная, \nд. 87, офис № 40",
                           reply_markup=keyboard.ikb_main)


@dp.message_handler(lambda message: "справочник" in message.text.lower())
async def push_info(message: types.Message):
    await bot.send_message(message.from_user.id, "Раздел находится в разработке",
                           reply_markup=keyboard.ikb_main)


@dp.message_handler(lambda message: "Оставить отзыв в 2Гис" in message.text)
async def push_2Gis(message: types.Message):
    await bot.send_message(message.from_user.id, "https://2gis.ru/tomsk/firm/70000001071171625?m=84.953548%2C56.503529%2F16",
                           reply_markup=keyboard.ikb_main)


@dp.message_handler(lambda message: "Связаться со специалистом компании" in message.text)
async def push_call(message: types.Message):
    await bot.send_message(message.from_user.id, "Выберите удобный способ связи",
                           reply_markup=keyboard.kb_call)
    await bot.send_message(message.from_user.id, "Для возврата в главное меню нажмите кнопку",
                           reply_markup=keyboard.ikb_main)

@dp.message_handler(lambda message: "Связаться самому" in message.text)
async def push_call_yourself(message: types.Message):
    await bot.send_message(message.from_user.id, "телефон компании - 666666\n"
                                                 "telegram - @karaperidol\n"
                                                 "watsapp - 89964147180",
                           reply_markup=keyboard.ikb_main)

@dp.message_handler(lambda message: "Услуги компании" in message.text)
async def push_works(message: types.Message):
    await bot.send_photo(message.from_user.id, "AgACAgIAAxkBAAIGO2RXa9dsSY7IHwlf8Lo3RqKFTNZ4AALZxzEba664SlvbqWQosWz_AQADAgADcwADLwQ",
                         "Биозащита СЭС - наша команда специализируется на профессиональном уничтожении любых "
                         "членистоногих вредителей, грызунов, вирусов, грибков и бактерий! Мастера имеют большой опыт "
                         "работы и гарантировано избавят от нежелательных соседей навсегда!",
                           reply_markup=keyboard.kb_works)
    await bot.send_message(message.from_user.id, "Для возврата в главное меню нажмите кнопку",
                           reply_markup=keyboard.ikb_main)



