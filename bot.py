from aiogram.utils import executor

import data_base
import keyboard
from create_bot import dp, bot
from aiogram import types

async def on_startup(_):
    data_base.db_start()
    print("Папа в здании")



@dp.message_handler(lambda message: "start" in message.text.lower())
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "салам, ты кто будешь?",
                           reply_markup=keyboard.kb_firstwindow)
    admins = await data_base.get_admins_list()
    print(admins)

@dp.message_handler(lambda message: message.text.lower() in ["частное лицо", "компания"])
async def go_to_main_fromstart(message: types.Message):
    await bot.send_message(message.from_user.id, "Здравствуй, дорогой друг! Будем травить!",
                           reply_markup=keyboard.kb_mainwindow)
    await data_base.user_add(message)

@dp.callback_query_handler(text="в начало")
async def go_to_main(message: types.Message):
    await bot.send_message(message.from_user.id, "Здравствуй, дорогой друг! Будем травить!",
                           reply_markup=keyboard.kb_mainwindow)

@dp.message_handler(lambda message: "адрес компании" in message.text.lower())
async def push_adress(message: types.Message):
    await bot.send_message(message.from_user.id, "г. Томск, ул. Большая Подгорная, \nд. 87, офис № 40",
                           reply_markup=keyboard.ikb_main)

@dp.message_handler(lambda message: "справочник" in message.text.lower())
async def push_info(message: types.Message):
    await bot.send_message(message.from_user.id, "Тараканы тобе отыбут хлеще хохлов, травить надо",
                           reply_markup=keyboard.ikb_main)

@dp.message_handler(lambda message: "Оставить отзыв в 2Гис" in message.text)
async def push_2Gis(message: types.Message):
    await bot.send_message(message.from_user.id, "Тут будет лежать ссылка на 2 гис, а эата для"
                                                 "тэста и радости https://www.pornhub.com/",
                           reply_markup=keyboard.ikb_main)

@dp.message_handler(lambda message: "Связаться со специалистом компании" in message.text)
async def push_call(message: types.Message):
    await bot.send_message(message.from_user.id, "Тут будут ссылки на компанию, кнопка на заявку звонка",
                           reply_markup=keyboard.ikb_main)

@dp.message_handler(lambda message: "Услуги компании" in message.text)
async def push_works(message: types.Message):
    await bot.send_message(message.from_user.id, "here wil be located main functions of company",
                           reply_markup=keyboard.ikb_main)
@dp.message_handler(content_types = ['photo'])
async def any_shit(message : types.Message, a="nnn"):
    await bot.send_message(message.from_user.id, message.photo[0].file_id)
    await bot.send_message(message.from_user.id, message.from_user.id)

@dp.message_handler(content_types = ['video'])
async def any_shit2(message : types.Message, a="nnn"):
    await bot.send_message(message.from_user.id, message.video.file_id)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True, on_startup = on_startup)