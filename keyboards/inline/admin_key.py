from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import value
from database import db_select_coupon, db_select_admins, db_user_info


# def choice_change_api_key():
#     return InlineKeyboardMarkup(2).add(
#         InlineKeyboardButton('BTC', callback_data=f'TRANSACTION:BTC'),
#         InlineKeyboardButton('LTC', callback_data=f'TRANSACTION:LTC')
#     )


# def quest_app(ids):
#     return InlineKeyboardMarkup(2).add(
#         InlineKeyboardButton('Подтвердить', callback_data=f'CLIENT_APP:YES:{ids}'),
#         InlineKeyboardButton('Отменить', callback_data=f'CLIENT_APP:NO:{ids}')
#     )


async def product_settings():
    markup = InlineKeyboardMarkup(2)
    button_1 = InlineKeyboardButton('Добавить продукт', callback_data='SET_ADD_PRODUCT')
    button_2 = InlineKeyboardButton('Добавить новый товар в продукт', callback_data='SET_ADD_ITEM')
    button_3 = InlineKeyboardButton('Удалить товар в продукте', callback_data='SET_DEL_ITEM')
    markup.add(button_1, button_2, button_3)
    return markup


async def coupon_settings():
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('Создать купон', callback_data='ADD_COUPON')
    button_2 = InlineKeyboardButton('Активные купоны', callback_data='INFO_COUPON')
    markup.add(button_1, button_2)
    return markup


async def coupon_info():
    coupon = db_select_coupon()
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        *[InlineKeyboardButton(f'{coupon[a][1]} - {coupon[a][2]} {value}', callback_data=f'COUPON:{coupon[a][0]}') for a
          in range(len(coupon))])
    return markup


async def catalog_settings():
    markup = InlineKeyboardMarkup(2)
    button_1 = InlineKeyboardButton('Добавить каталог', callback_data='SET_ADD_CATALOG')
    button_2 = InlineKeyboardButton('Удалить каталог', callback_data='SET_DEL_CATALOG')
    button_3 = InlineKeyboardButton('Добавить подкаталог', callback_data='SET_ADD_SUBCATALOG')
    button_4 = InlineKeyboardButton('Удалить подкаталог', callback_data='SET_DEL_SUBCATALOG')
    markup.add(button_1, button_2, button_3, button_4)
    return markup


async def accept_or_not():
    markup = InlineKeyboardMarkup(2)
    button_1 = InlineKeyboardButton('Принять', callback_data='ACCEPT')
    button_2 = InlineKeyboardButton('Отменить', callback_data='CANCEL')
    markup.add(button_1, button_2)
    return markup


async def del_items(prod_id, photo=None):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Удалить данные', callback_data=f'SET_DEL_ITEM:{prod_id}:{photo}'))
    return markup


async def stat_key():
    return InlineKeyboardMarkup(2).add(
        InlineKeyboardButton('Администратор', callback_data='STAT:ADMIN'),
        InlineKeyboardButton('Операции', callback_data='STAT:TOPUP')
    )


async def choice_admin():
    markup = InlineKeyboardMarkup(3)
    admins = db_select_admins()
    markup.add(
        *[InlineKeyboardButton(f'{db_user_info(_[0])[1]} | {_[0]}', callback_data=f'STATISTIC_ADMIN:{_[0]}') for _ in admins])
    return markup


async def change_bal_key(user_id):
    return InlineKeyboardMarkup(1).add(
        InlineKeyboardButton('Изменить баланс', callback_data=f'CHANGE_BALANCE_USER:{user_id}')
    )
