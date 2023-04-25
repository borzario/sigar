from aiogram.utils import executor

import data_base
from create_bot import dp, bot
from aiogram import types
from functional import client, admin
from handlers import h_admin, h_client, h_all




async def on_startup(_):
    data_base.db_start()
    print("Папа в здании")


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