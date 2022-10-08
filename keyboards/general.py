from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import value
from database import db_select_subcatalog, db_select_catalog, db_select_polls_botadmins, db_select_product, db_select_item


async def cancel():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Cancel', callback_data='CANCEL'))
    return markup


async def subcatalog_list(callback, id, user_id, pos=None, admin=None):
    subcatalog = db_select_subcatalog(cat_id=id)
    products = db_select_product(f'0:{id}')
    markup = InlineKeyboardMarkup(2)
    key_list = []
    if db_select_polls_botadmins(user_id):
        markup.add(*[InlineKeyboardButton(sub[2], callback_data=f'{callback}_{id}_{sub[0]}') for sub in subcatalog])
    else:
        for sub in subcatalog:
            for product in db_select_product(sub[0]):
                if len(db_select_item(product[0])) > 0:
                    key_list.append(InlineKeyboardButton(sub[2], callback_data=f'{callback}_{id}_{sub[0]}'))
                    break
        markup.add(*[button for button in key_list])
    markup.add(*[InlineKeyboardButton(f'{prod[2]} - {prod[4]}{value}', callback_data=f'PRODUCT:{prod[0]}') for prod in
                 products if admin or len(db_select_item(prod[0]))])

    if pos == 'user':
        markup.add(InlineKeyboardButton('Back', callback_data=f'BACK_CATALOG'))
    elif pos == 'admin':
        markup.add(InlineKeyboardButton('➕ Добавит продукт', callback_data=f'SET_ADD_PRODUCT_SUBCATALOG_0{id}'))
        markup.add(InlineKeyboardButton('Back', callback_data='SET_ADD_PRODUCT'))
    return markup


async def catalog(callback, back):
    markup = InlineKeyboardMarkup(row_width=2)
    db_catalog = db_select_catalog()

    markup.add(*[InlineKeyboardButton(db_catalog[a][1], callback_data=f'{callback}{db_catalog[a][0]}') for a in
                 range(len(db_catalog))])
    if back is not None:
        markup.add(InlineKeyboardButton('Back', callback_data=back))
    return markup


async def accept_buy_or(user, prod, subcat_id, cat):
    markup = InlineKeyboardMarkup(row_width=2)
    get_admin = db_select_polls_botadmins(user)
    if get_admin:
        if get_admin[1] == 2:
            markup.add(InlineKeyboardButton('🆕 Добавить данные', callback_data=f'SET_ADD_ITEM:{prod}'))
            markup.add(InlineKeyboardButton('❌ Удалить', callback_data=f'SET_DEl_PRODUCT:{prod}'),
                       InlineKeyboardButton('ℹ️ Данные', callback_data=f'SET_DATA_PRODUCT:{prod}'))
    button_1 = InlineKeyboardButton('✅ Buy', callback_data=f'GO_BUY:{prod}')
    button_2 = InlineKeyboardButton('↩️ Back', callback_data=f'BACK_SUBCATALOG_{cat}_{subcat_id}')
    markup.add(button_1, button_2)
    return markup
