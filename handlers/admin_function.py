# -*- coding: UTF-8 -*-
import datetime
import sqlite3

from aiogram.utils.markdown import escape_md

from config import cover_img, db
from database import db_insert_catalog, db_delete_catalog, db_insert_subcatalog, db_delete_subcatalog, \
    db_select_subcatalog, db_insert_product, db_delete_product, db_insert_item, db_insert_client, db_insert_coupon, \
    db_delete_coupon, db_select_item, db_del_item, db_select_all_user, db_insert_history_admin, db_select_history_admin, \
    db_select_product, db_delete_history_admin, db_user_info, db_update_app, dp_select_app, db_user_insert, \
    select_date_top_up
from keyboards import catalog, db_select_catalog, subcatalog_list, accept_or_not, cancel, coupon_info, del_items, \
    change_bal_key, choice_admin
from loader import dp, bot
from aiogram.types import CallbackQuery
from states import settAdmin, changeCoinbase, transaction, spam, SearchUser, ChangeUser, SellAdminState
from aiogram import types
from aiogram.dispatcher import FSMContext


####################################################################################################
# CALLBACK HANDLER
####################################################################################################



@dp.callback_query_handler(text_startswith='CLIENT_APP:', state='*')
async def admin_client_app(call: CallbackQuery, state: FSMContext):
    _, method, ids = call.data.split(':')
    app = dp_select_app(ids)
    if method == 'YES':
        db_update_app(ids, 1)
        await state.update_data(ids=ids)
        await call.message.answer('Введите сумму выплаты')
        await SellAdminState.amount.set()
    else:
        await call.message.delete()
        await call.answer('Вы отменили заявку')
        await bot.send_message(app[0], 'Ваша заявка на продажу отклонена')

