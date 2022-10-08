from aiogram.types import CallbackQuery
from database import db_select_polls_botadmins
from keyboards import product_settings, coupon_settings, catalog_settings, cancel, choice_admin
from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from states import changeCoinbase, spam, SearchUser


class isAdmins(BoundFilter):
    async def check(self, message: types.Message):
        if db_select_polls_botadmins(message.from_user.id) is None:
            return False
        else:
            return True


@dp.message_handler(isAdmins(), text='Настройка продуктов')
async def settings_product(msg: types.Message):
    await bot.delete_message(msg.chat.id, msg.message_id)
    await msg.answer('Настройка продуктов', reply_markup=await product_settings())


@dp.message_handler(isAdmins(), text='Настройка каталога')
async def settings_catalog(msg: types.Message):
    await bot.delete_message(msg.chat.id, msg.message_id)
    await msg.answer('Настройка каталога', reply_markup=await catalog_settings())


@dp.message_handler(isAdmins(), text='Сделать рассылку')
async def get_spam(msg: types.Message):
    await msg.answer('Ожидаю от вас пост для рассылки')
    await spam.post.set()


@dp.message_handler(commands=['chatID', 'help'])
async def send_welcome(message: types.Message):    
    await message.reply(message.chat.id)



@dp.message_handler(isAdmins(), text='Пользователь')
async def user_info(msg: types.Message):
    await msg.answer('Введите *ID* пользователя')
    await SearchUser.id.set()


# state
@dp.callback_query_handler(text='BACK_SETTINGS_CATALOG')
async def set_del_subcatalog(call: CallbackQuery):
    await bot.edit_message_text('Настройка каталога', call.from_user.id, call.message.message_id,
                                reply_markup=await catalog_settings())


@dp.callback_query_handler(text='BACK_SETTINGS_PRODUCT')
async def set_del_subcatalog(call: CallbackQuery):
    await bot.edit_message_text('Настройка продуктов', call.from_user.id, call.message.message_id,
                                reply_markup=await product_settings())
