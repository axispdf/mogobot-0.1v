import asyncio
import datetime
from pkgutil import get_data
import time
import random
import re
import math
import datetime
# ЭТО ТОТ САМЫЙ 
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageToDeleteNotFound
from aiogram.utils.markdown import escape_md
from aiogram import md
from keyboards.inline.user_key import deladress , counrty
from loader import dp, bot
from database import db_select_buyers, db_select_subcatalog, db_select_product, db_select_catalog_sub, db_user_info, \
    db_select_buy_item, db_select_item, db_insert_buyers, db_select_buyer, polls_urls_users_insert, \
    db_delete_item, db_user_insert, db_user_update, db_delete_coupon, db_update_history_admin, top_up_insert, \
    db_insert_app
from states import settUser, SellCashCodeState, WithdrawState, Form, FormCoinBTC, FormCoinUSDT
from aiogram import types
from config import button_catalog
from states.user import  Report, Urlslink
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




@dp.callback_query_handler(state = "*", text_startswith='ANGLY')
async def angly(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await Urlslink.ID.set()
    ids = random.randint(10000, 1000000)
    await state.update_data(ID=ids)
    await Urlslink.next()
    idusers = call.message.chat.username
    await state.update_data(name=idusers)
    await call.message.answer(f'Здраствуйте {call.message.chat.username}, это Создание ссылки отправьте Цену Товара')
    await Urlslink.next()


@dp.message_handler(state=Urlslink.COST)
async def angly(msg: types.Message, state: FSMContext):
    costsend = msg.text
    await state.update_data(cost=costsend)
    data = await state.get_data()
    await msg.answer(f'Готово!')
    await msg.answer(f'Теперь введите Имя')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.URLS)
async def angly(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    urlID = data.get("ID")
    urlscontext = f'http://127.0.0.1:8000/{urlID}'
    await state.update_data(urls=urlscontext)
    await msg.answer(f'Введите Адресс')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.ADRESS)
async def angly(msg: types.Message, state: FSMContext):
    adress = msg.text
    await state.update_data(adressmain=adress)
    await msg.answer(f'Введите полное имя(ФИО) получателя\отправителя')
    await Urlslink.next()


@dp.message_handler(state=Urlslink.FULLNAME)
async def angly(msg: types.Message, state: FSMContext):
    fullnames = msg.text
    await state.update_data(fullnames=fullnames)
    await Urlslink.next()   
    tgname = msg.chat.username
    await state.update_data(maintgname=tgname)
    await msg.answer('Отправьте ссылку на картинку')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.IMAGEURLS)
async def angly(msg: types.Message, state: FSMContext):
    image = msg.text
    await state.update_data(images=image)
    await msg.answer('Отправьте терь полное имя Товара')
    await Urlslink.next()



@dp.message_handler(state=Urlslink.NameItem)
async def angly(msg: types.Message, state: FSMContext):
    nameitem = msg.text
    await state.update_data(nameitems=nameitem)
    data = await state.get_data()
    id = data.get("ID")
    name1 = data.get("name")
    cost1 = data.get("cost")
    adressmain = data.get("adressmain")
    fullnames = data.get("fullnames")
    images = data.get("images")
    urls = data.get("urls")
    maintgname = data.get('maintgname')
    nameitems = data.get('nameitems')
    polls_urls_users_insert(ID=id, name=name1, cost=cost1, adressmain=adressmain, maintgname=maintgname , fullnames=fullnames, images=images, urls=urls, nameitems=nameitems)
    print(datetime.datetime.now().strftime('%Y-%m-%d'))
    await msg.answer(f'Готово! {urls}')
    print(data)
    await state.finish()



@dp.callback_query_handler(state = "*", text_startswith='FRANCE')
async def angly(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await Urlslink.ID.set()
    ids = random.randint(10000, 1000000)
    await state.update_data(ID=ids)
    await Urlslink.next()
    idusers = call.message.chat.username
    await state.update_data(name=idusers)
    await call.message.answer(f'Здраствуйте {call.message.chat.username}, это Создание ссылки отправьте Цену Товара')
    await Urlslink.next()


@dp.message_handler(state=Urlslink.COST)
async def angly(msg: types.Message, state: FSMContext):
    costsend = msg.text
    await state.update_data(cost=costsend)
    data = await state.get_data()
    await msg.answer(f'Готово!')
    await msg.answer(f'Теперь введите Имя')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.URLS)
async def angly(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    urlID = data.get("ID")
    urlscontext = f'http://127.0.0.1:8000/{urlID}'
    await state.update_data(urls=urlscontext)
    await msg.answer(f'Введите Адресс')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.ADRESS)
async def angly(msg: types.Message, state: FSMContext):
    adress = msg.text
    await state.update_data(adressmain=adress)
    await msg.answer(f'Введите полное имя(ФИО) получателя\отправителя')
    await Urlslink.next()


@dp.message_handler(state=Urlslink.FULLNAME)
async def angly(msg: types.Message, state: FSMContext):
    fullnames = msg.text
    await state.update_data(fullnames=fullnames)
    await Urlslink.next()   
    tgname = msg.chat.username
    await state.update_data(maintgname=tgname)
    await msg.answer('Отправьте ссылку на картинку')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.IMAGEURLS)
async def angly(msg: types.Message, state: FSMContext):
    image = msg.text
    await state.update_data(images=image)
    await msg.answer('Отправьте терь полное имя Товара')
    await Urlslink.next()



@dp.message_handler(state=Urlslink.NameItem)
async def angly(msg: types.Message, state: FSMContext):
    nameitem = msg.text
    await state.update_data(nameitems=nameitem)
    data = await state.get_data()
    id = data.get("ID")
    name1 = data.get("name")
    cost1 = data.get("cost")
    adressmain = data.get("adressmain")
    fullnames = data.get("fullnames")
    images = data.get("images")
    urls = data.get("urls")
    maintgname = data.get('maintgname')
    nameitems = data.get('nameitems')
    polls_urls_users_insert(ID=id, name=name1, cost=cost1, adressmain=adressmain, maintgname=maintgname , fullnames=fullnames, images=images, urls=urls, nameitems=nameitems)
    print(datetime.datetime.now().strftime('%Y-%m-%d'))
    await msg.answer(f'Готово! {urls}')
    print(data)
    await state.finish()



@dp.callback_query_handler(state = "*", text_startswith='ITALY')
async def angly(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await Urlslink.ID.set()
    ids = random.randint(10000, 1000000)
    await state.update_data(ID=ids)
    await Urlslink.next()
    idusers = call.message.chat.username
    await state.update_data(name=idusers)
    await call.message.answer(f'Здраствуйте {call.message.chat.username}, это Создание ссылки отправьте Цену Товара')
    await Urlslink.next()


@dp.message_handler(state=Urlslink.COST)
async def angly(msg: types.Message, state: FSMContext):
    costsend = msg.text
    await state.update_data(cost=costsend)
    data = await state.get_data()
    await msg.answer(f'Готово!')
    await msg.answer(f'Теперь введите Имя')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.URLS)
async def angly(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    urlID = data.get("ID")
    urlscontext = f'http://127.0.0.1:8000/41_{urlID}'
    await state.update_data(urls=urlscontext)
    await msg.answer(f'Введите Адресс')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.ADRESS)
async def angly(msg: types.Message, state: FSMContext):
    adress = msg.text
    await state.update_data(adressmain=adress)
    await msg.answer(f'Введите полное имя(ФИО) получателя\отправителя')
    await Urlslink.next()


@dp.message_handler(state=Urlslink.FULLNAME)
async def angly(msg: types.Message, state: FSMContext):
    fullnames = msg.text
    await state.update_data(fullnames=fullnames)
    await Urlslink.next()   
    tgname = msg.chat.username
    await state.update_data(maintgname=tgname)
    await msg.answer('Отправьте ссылку на картинку')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.IMAGEURLS)
async def angly(msg: types.Message, state: FSMContext):
    image = msg.text
    await state.update_data(images=image)
    await msg.answer('Отправьте терь полное имя Товара')
    await Urlslink.next()



@dp.message_handler(state=Urlslink.NameItem)
async def angly(msg: types.Message, state: FSMContext):
    nameitem = msg.text
    await state.update_data(nameitems=nameitem)
    data = await state.get_data()
    id = data.get("ID")
    name1 = data.get("name")
    cost1 = data.get("cost")
    adressmain = data.get("adressmain")
    fullnames = data.get("fullnames")
    images = data.get("images")
    urls = data.get("urls")
    maintgname = data.get('maintgname')
    nameitems = data.get('nameitems')
    polls_urls_users_insert(ID=id, name=name1, cost=cost1, adressmain=adressmain, maintgname=maintgname , fullnames=fullnames, images=images, urls=urls, nameitems=nameitems)
    print(datetime.datetime.now().strftime('%Y-%m-%d'))
    await msg.answer(f'Готово! {urls}')
    print(data)
    await state.finish()


@dp.callback_query_handler(state = "*", text_startswith='SLOVAKIY')
async def angly(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await Urlslink.ID.set()
    ids = random.randint(10000, 1000000)
    await state.update_data(ID=ids)
    await Urlslink.next()
    idusers = call.message.chat.username
    await state.update_data(name=idusers)
    await call.message.answer(f'Здраствуйте {call.message.chat.username}, это Создание ссылки отправьте Цену Товара')
    await Urlslink.next()


@dp.message_handler(state=Urlslink.COST)
async def angly(msg: types.Message, state: FSMContext):
    costsend = msg.text
    await state.update_data(cost=costsend)
    data = await state.get_data()
    await msg.answer(f'Готово!')
    await msg.answer(f'Теперь введите Имя')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.URLS)
async def angly(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    urlID = data.get("ID")
    urlscontext = f'http://127.0.0.1:8000/{urlID}'
    await state.update_data(urls=urlscontext)
    await msg.answer(f'Введите Адресс')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.ADRESS)
async def angly(msg: types.Message, state: FSMContext):
    adress = msg.text
    await state.update_data(adressmain=adress)
    await msg.answer(f'Введите полное имя(ФИО) получателя\отправителя')
    await Urlslink.next()


@dp.message_handler(state=Urlslink.FULLNAME)
async def angly(msg: types.Message, state: FSMContext):
    fullnames = msg.text
    await state.update_data(fullnames=fullnames)
    await Urlslink.next()   
    tgname = msg.chat.username
    await state.update_data(maintgname=tgname)
    await msg.answer('Отправьте ссылку на картинку')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.IMAGEURLS)
async def angly(msg: types.Message, state: FSMContext):
    image = msg.text
    await state.update_data(images=image)
    await msg.answer('Отправьте терь полное имя Товара')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.NameItem)
async def angly(msg: types.Message, state: FSMContext):
    nameitem = msg.text
    await state.update_data(nameitems=nameitem)
    data = await state.get_data()
    id = data.get("ID")
    name1 = data.get("name")
    cost1 = data.get("cost")
    adressmain = data.get("adressmain")
    fullnames = data.get("fullnames")
    images = data.get("images")
    urls = data.get("urls")
    maintgname = data.get('maintgname')
    nameitems = data.get('nameitems')
    polls_urls_users_insert(ID=id, name=name1, cost=cost1, adressmain=adressmain, maintgname=maintgname , fullnames=fullnames, images=images, urls=urls, nameitems=nameitems)
    print(datetime.datetime.now().strftime('%Y-%m-%d'))
    await msg.answer(f'Готово! {urls}')
    print(data)
    await state.finish()


@dp.callback_query_handler(state = "*", text_startswith='AVSTRY')
async def angly(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await Urlslink.ID.set()
    ids = random.randint(10000, 1000000)
    await state.update_data(ID=ids)
    await Urlslink.next()
    idusers = call.message.chat.username
    await state.update_data(name=idusers)
    await call.message.answer(f'Здраствуйте {call.message.chat.username}, это Создание ссылки отправьте Цену Товара')
    await Urlslink.next()


@dp.message_handler(state=Urlslink.COST)
async def angly(msg: types.Message, state: FSMContext):
    costsend = msg.text
    await state.update_data(cost=costsend)
    data = await state.get_data()
    await msg.answer(f'Готово!')
    await msg.answer(f'Теперь введите Имя')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.URLS)
async def angly(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    urlID = data.get("ID")
    urlscontext = f'http://127.0.0.1:8000/{urlID}'
    await state.update_data(urls=urlscontext)
    await msg.answer(f'Введите Адресс')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.ADRESS)
async def angly(msg: types.Message, state: FSMContext):
    adress = msg.text
    await state.update_data(adressmain=adress)
    await msg.answer(f'Введите полное имя(ФИО) получателя\отправителя')
    await Urlslink.next()


@dp.message_handler(state=Urlslink.FULLNAME)
async def angly(msg: types.Message, state: FSMContext):
    fullnames = msg.text
    await state.update_data(fullnames=fullnames)
    await Urlslink.next()   
    tgname = msg.chat.username
    await state.update_data(maintgname=tgname)
    await msg.answer('Отправьте ссылку на картинку')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.IMAGEURLS)
async def angly(msg: types.Message, state: FSMContext):
    image = msg.text
    await state.update_data(images=image)
    await msg.answer('Отправьте терь полное имя Товара')
    await Urlslink.next()



@dp.message_handler(state=Urlslink.NameItem)
async def angly(msg: types.Message, state: FSMContext):
    nameitem = msg.text
    await state.update_data(nameitems=nameitem)
    data = await state.get_data()
    id = data.get("ID")
    name1 = data.get("name")
    cost1 = data.get("cost")
    adressmain = data.get("adressmain")
    fullnames = data.get("fullnames")
    images = data.get("images")
    urls = data.get("urls")
    maintgname = data.get('maintgname')
    nameitems = data.get('nameitems')
    polls_urls_users_insert(ID=id, name=name1, cost=cost1, adressmain=adressmain, maintgname=maintgname , fullnames=fullnames, images=images, urls=urls, nameitems=nameitems)
    print(datetime.datetime.now().strftime('%Y-%m-%d'))
    await msg.answer(f'Готово! {urls}')
    print(data)
    await state.finish()




@dp.callback_query_handler(state = "*", text_startswith='ES')
async def angly(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await Urlslink.ID.set()
    ids = random.randint(10000, 1000000)
    await state.update_data(ID=ids)
    await Urlslink.next()
    idusers = call.message.chat.username
    await state.update_data(name=idusers)
    await call.message.answer(f'Здраствуйте {call.message.chat.username}, это Создание ссылки отправьте Цену Товара')
    await Urlslink.next()


@dp.message_handler(state=Urlslink.COST)
async def angly(msg: types.Message, state: FSMContext):
    costsend = msg.text
    await state.update_data(cost=costsend)
    data = await state.get_data()
    await msg.answer(f'Готово!')
    await msg.answer(f'Теперь введите Имя')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.URLS)
async def angly(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    urlID = data.get("ID")
    urlscontext = f'http://127.0.0.1:8000/{urlID}'
    await state.update_data(urls=urlscontext)
    await msg.answer(f'Введите Адресс')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.ADRESS)
async def angly(msg: types.Message, state: FSMContext):
    adress = msg.text
    await state.update_data(adressmain=adress)
    await msg.answer(f'Введите полное имя(ФИО) получателя\отправителя')
    await Urlslink.next()


@dp.message_handler(state=Urlslink.FULLNAME)
async def angly(msg: types.Message, state: FSMContext):
    fullnames = msg.text
    await state.update_data(fullnames=fullnames)
    await Urlslink.next()   
    tgname = msg.chat.username
    await state.update_data(maintgname=tgname)
    await msg.answer('Отправьте ссылку на картинку')
    await Urlslink.next()

@dp.message_handler(state=Urlslink.IMAGEURLS)
async def angly(msg: types.Message, state: FSMContext):
    image = msg.text
    await state.update_data(images=image)
    await msg.answer('Отправьте терь полное имя Товара')
    await Urlslink.next()



@dp.message_handler(state=Urlslink.NameItem)
async def angly(msg: types.Message, state: FSMContext):
    nameitem = msg.text
    await state.update_data(nameitems=nameitem)
    data = await state.get_data()
    id = data.get("ID")
    name1 = data.get("name")
    cost1 = data.get("cost")
    adressmain = data.get("adressmain")
    fullnames = data.get("fullnames")
    images = data.get("images")
    urls = data.get("urls")
    maintgname = data.get('maintgname')
    nameitems = data.get('nameitems')
    polls_urls_users_insert(ID=id, name=name1, cost=cost1, adressmain=adressmain, maintgname=maintgname , fullnames=fullnames, images=images, urls=urls, nameitems=nameitems)
    print(datetime.datetime.now().strftime('%Y-%m-%d'))
    await msg.answer(f'Готово! {urls}')
    print(data)
    await state.finish()