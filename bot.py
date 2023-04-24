from aiogram.utils import executor

import data_base
import keyboard
import list_of_admins
from create_bot import dp, bot
from aiogram import types
from functional import client, admin


async def on_startup(_):
    data_base.db_start()
    print("Папа в здании")


@dp.message_handler(lambda message: "start" in message.text.lower())
async def start(message: types.Message):
    if str(message.from_user.id) in list_of_admins.admins:
        await bot.send_message(message.from_user.id, "choose your status",
                               reply_markup=keyboard.kb_admin_first)
    else:
        await bot.send_message(message.from_user.id, "салам, ты кто будешь?",
                           reply_markup=keyboard.kb_firstwindow)


@dp.message_handler(lambda message: message.text.lower() in ["частное лицо", "компания"])
async def go_to_main_fromstart(message: types.Message):
    await bot.send_message(message.from_user.id, "Здравствуй, дорогой друг! Будем травить!",
                           reply_markup=keyboard.kb_mainwindow)
    await data_base.user_add(message)


@dp.callback_query_handler(text="в начало")
@dp.message_handler(lambda message: "user" == message.text.lower())
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
    await bot.send_message(message.from_user.id, "Выберите удобный способ связи",
                           reply_markup=keyboard.kb_call)
    await bot.send_message(message.from_user.id, "Для возврата в главное меню нажмите кнопоньку",
                           reply_markup=keyboard.ikb_main)

@dp.message_handler(lambda message: "Связаться самому" in message.text)
async def push_call_yourself(message: types.Message):
    await bot.send_message(message.from_user.id, "телефон компании - 666666\n"
                                                 "telegram - @karaperidol\n"
                                                 "watsapp - 89964147180",
                           reply_markup=keyboard.ikb_main)

@dp.message_handler(lambda message: "Услуги компании" in message.text)
async def push_works(message: types.Message):
    await bot.send_message(message.from_user.id, "here wil be located main functions of company",
                           reply_markup=keyboard.ikb_main)


@dp.message_handler(content_types=['photo'])
async def any_shit(message : types.Message, a="nnn"):
    await bot.send_message(message.from_user.id, message.photo[0].file_id)
    await bot.send_message(message.from_user.id, message.from_user.id)


@dp.message_handler(content_types=['video'])
async def any_shit2(message : types.Message, a="nnn"):
    await bot.send_message(message.from_user.id, message.video.file_id)

client.registr_client(dp)
admin.registr_admin(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)