import asyncio
import datetime
from pkgutil import get_data
import time
import random
import re
import math
# ЭТО ТОТ САМЫЙ 
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageToDeleteNotFound
from aiogram.utils.markdown import escape_md
from aiogram import md
from keyboards.inline.user_key import deladress , counrty
from loader import dp, bot
from database import db_select_buyers, db_select_subcatalog, db_select_product, db_select_catalog_sub, db_user_info, \
    db_select_buy_item, db_select_item, db_insert_buyers, db_select_buyer, \
    db_delete_item, db_user_insert, db_user_update, db_delete_coupon, db_update_history_admin, top_up_insert, \
    db_insert_app, db_update_adress
from states import settUser, SellCashCodeState, WithdrawState, Form, FormCoinBTC, FormCoinUSDT
from aiogram import types
from config import button_catalog
from states.user import DAdress, Report
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


# CALLBACK HANDLER


def is_number(_str):
    try:
        int(_str)
        return True
    except ValueError:
        return False



@dp.message_handler(text='ХУЙ', state = "*")
async def bug_reports(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Send your bug report.')
    await Report.text.set()



@dp.callback_query_handler(state = "*", text_startswith='BUG_REPORTS')
async def bug_reports(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer('Send your bug report.')
    await Report.text.set()


@dp.message_handler(state=Report.text)
async def bug_reports1(message: types.Message, state: FSMContext):
    await message.delete()

    answer = message.text
    await state.update_data(answer1=answer)

    data = await state.get_data()
    dataaccept = data.get("answer1")

    reportbchatid = -697631872
    await bot.send_message(chat_id=reportbchatid, text=f'New bug report:\n {dataaccept} \nот: @{message.chat.username}\nID: {message.chat.id}\n')
    
    await state.finish()
    await message.answer('Report was successful sent. Thanks a lot!')




@dp.message_handler(state="*", text=button_catalog)
async def menucountry(message: types.Message, state: FSMContext):
    await message.answer('Выбери страну: ', reply_markup= await counrty())
