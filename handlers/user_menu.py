# - *- coding: utf- 8 - *-
from ast import Call
from cgitb import text
import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from config import button_profile, button_availability, work
from database import db_user_info, db_select_catalog
from keyboards import catalog
from keyboards.inline.user_key import *
from loader import dp, bot


@dp.message_handler(text=button_profile, state='*')
async def user_profile(msg: types.Message, state: FSMContext):
    await state.finish()
    await bot.delete_message(msg.chat.id, msg.message_id)
    user = db_user_info(msg.chat.id)
    if not user:
        await bot.send_message(msg.chat.id, 'Please enter /start')
        return
    await bot.send_message(msg.chat.id, f'👤 Profile: {user[1]}\n\n'
                                        f'\n✨ Registration: {user[2]}\n',
                           reply_markup=await profile(msg.chat.id))



@dp.message_handler(text=button_availability, state='*')
async def user_help(msg: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_photo(msg.chat.id, open(work, 'rb'), caption='WORK WORK WORK')

    

@dp.callback_query_handler(text_startswith='BACK_CATALOG')
async def user_view_pos(call: CallbackQuery):
    pass