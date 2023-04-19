from aiogram.utils import executor

import keyboard
from create_bot import dp, bot
from aiogram import types

async def on_startup(_):
    print("Папа в здании")


@dp.message_handler(lambda message: "start" in message.text.lower())
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Здравствуй, дорогой друг! Будем травить!",
                           reply_markup=keyboard.kb_mainwindow)


@dp.message_handler(content_types = ['photo'])
async def any_shit(message : types.Message, a="nnn"):
    await bot.send_message(message.from_user.id, message.photo[0].file_id)
    await bot.send_message(message.from_user.id, message.from_user.id)

@dp.message_handler(content_types = ['video'])
async def any_shit2(message : types.Message, a="nnn"):
    await bot.send_message(message.from_user.id, message.video.file_id)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True, on_startup = on_startup)