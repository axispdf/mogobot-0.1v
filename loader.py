# - *- coding: utf- 8 - *-
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import token_bot
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=token_bot, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
