from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import tgcoin

storage = MemoryStorage()
bot = Bot(token=tgcoin.TOKEN)
dp = Dispatcher(bot, storage=storage)
