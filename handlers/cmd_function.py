import asyncio

from aiogram.dispatcher import FSMContext

from config import reg_text, auth_text, INFO_BOT_TEXT
from database import db_user_info, db_user_reg, db_insert_admin, db_delete_admin, db_select_polls_botadmins, top_up_select, db_select_profile_auto
from loader import dp, bot
from keyboards import main_start


@dp.message_handler(commands=['start'], state='*')
@dp.throttled(lambda msg, loop, *args, **kwargs: loop.create_task(bot.send_message(msg.from_user.id, "Перестань "
                                                                                                     "флудить!")),
              rate=5)
async def start_for_user(msg, state: FSMContext):
    await state.finish()
    if not db_user_info(msg.chat.id):
        db_user_reg(msg)
        await msg.answer(reg_text, reply_markup=await main_start(msg.chat.id))
    else:
        await msg.answer(auth_text, reply_markup=await main_start(msg.chat.id))


@dp.message_handler(commands=['info'], state='*')
async def info_user(msg, state: FSMContext):
    await state.finish()
    data = msg.text.split()
    if db_select_polls_botadmins(msg.chat.id):
        if len(data) > 1:
            text = ''
            top_up_user = top_up_select(data[1])
            if not top_up_user:
                await msg.answer('Информация не найдена')
            for info in top_up_user:
                text += f'{info[0]}, {info[1]}, {info[2]}\n'
            await msg.answer(text)
        else:
            await msg.answer('*SYSTEM:* /info [[user_id]]')


@dp.message_handler(commands=['infobot'], state='*')
async def info_user(msg, state: FSMContext):
    await msg.answer(INFO_BOT_TEXT)


@dp.message_handler(commands=['add_admin'])
async def add_admin(msg):
    if db_select_polls_botadmins(msg.chat.id):
        data = msg.text.split()
        if len(data) > 1:
            new_admin_id = data[1]
            if db_user_info(new_admin_id):
                db_insert_admin(new_admin_id)
                await msg.answer('*SYSTEM:* Администратор успешно добавлен')
            else:
                await msg.answer('*SYSTEM:* Пользователь не найден.\n\n'
                                 '*Будущий администратор должен быть зарегистрирован с помощью команды /start*')
        else:
            await msg.answer('*SYSTEM:* /add\\_admin [[user_id]]')


@dp.message_handler(commands=['del_admin'])
async def del_admin(msg):
    if db_select_polls_botadmins(msg.chat.id):
        data = msg.text.split()
        if len(data) > 1:
            old_admin_id = data[1]
            if db_user_info(old_admin_id):
                db_delete_admin(old_admin_id)
                await msg.answer('*SYSTEM:* Администратор успешно удален')
            else:
                await msg.answer('*SYSTEM:* Пользователь не найден.')
        else:
            await msg.answer('*SYSTEM:* /del\\_admin [[user_id]]')


# @dp.message_handler(commands=['myprofiles'], state='*')
# async def def_info_user(msg, state: FSMContext):
#     await state.finish()
#     print('ЗАПУСК ФУНКЦИЙ')
#     print(db_select_profile_auto(msg.chat.id))


@dp.message_handler(commands=['myprofiles'], state='*')
async def def_info_user(msg, state: FSMContext):
    await state.finish()
    if not db_user_info(msg.chat.id):
        db_user_reg(msg)
        await msg.answer(reg_text, reply_markup=await main_start(msg.chat.id))
    else:
        p = db_select_profile_auto(msg.chat.id)
        for item in p:
            address = (item)[-2]
            fullname = (item)[-1]
            print(f'ЭТО АДРЕСС {address}')
            print(f'ЭТО ПОЛНОЕ ИМЯ {fullname}')


