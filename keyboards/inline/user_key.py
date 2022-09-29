from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import value, KEYBOARD_STATUS
from database import db_select_buyers, db_select_product, db_select_item, db_select_admins


def choice_curr(curr):
    return InlineKeyboardMarkup(2).add(
        InlineKeyboardButton('BTC', callback_data=f'BTC'),
        InlineKeyboardButton('tether', callback_data=f'LTC'),
    )

def qiwi(curr):
    pass
    #   return InlineKeyboardMarkup(2).add(
    # )

        

def link_key(link):
    return InlineKeyboardMarkup(2).add(
        InlineKeyboardButton('Transaction Link', url=link)
    )


async def profile(u_id):
    profile_menu = InlineKeyboardMarkup(row_width=1)
    profile_menu.add(
        InlineKeyboardButton('Скрыть Ник', callback_data='NICKNAME'),
        InlineKeyboardButton('Скрыть Сервисы', callback_data='SERVIECE'),
        InlineKeyboardButton('Мои Профиля', callback_data='PROFILES'),
        InlineKeyboardButton('Back', callback_data='BACK_PROFILE')
    )
    if (KEYBOARD_STATUS == 1 and db_select_admins(u_id)) or KEYBOARD_STATUS == 2:
        profile_menu.add(
            InlineKeyboardButton('Conclusion', callback_data='WITHDRAW'),
            InlineKeyboardButton('Sell the cache code', callback_data='SELL_CASH_CODE')
        )
    return profile_menu


async def buyers_list(user, back=None):
    markup = InlineKeyboardMarkup(row_width=2)
    db_buyers = db_select_buyers(user)
    if back:
        markup.add(InlineKeyboardButton('Back', callback_data='ORDERS'))
        return markup
    markup.add(*[InlineKeyboardButton(db_buyers[a][2], callback_data=f'PURCHASED_{db_buyers[a][4]}') for a in
                 range(len(db_buyers))])
    markup.add(InlineKeyboardButton('Back', callback_data='BACK_PROFILE'))
    return markup


async def all_product(id, cat_id, admin):
    markup = InlineKeyboardMarkup(row_width=2)
    products = db_select_product(id)
    markup.add(*[InlineKeyboardButton(f'{product[2]} - {product[4]}{value}',
                                      callback_data=f'PRODUCT:{product[0]}') for product in products if
                 admin or len(db_select_item(product[0]))])
    markup.add(InlineKeyboardButton('Back', callback_data=f'ID_CATALOG_{cat_id}'))
    return markup


async def count_buy(product_id):
    markup = InlineKeyboardMarkup(row_width=3)
    button_1 = InlineKeyboardButton('✅OK', callback_data=f'BUY:1:{product_id}')
    markup.add(button_1)
    return markup


async def check_pay(curr, price=None):
    markup = InlineKeyboardMarkup(row_width=2)
    button_1 = InlineKeyboardButton('Check the payment', callback_data=f'CHECK_PAY:{curr}:{price}')
    markup.add(button_1)
    return markup



async def check_addres():
    markup = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('✅OK', callback_data='CHEACK_ADDRESS')
    markup.add(InlineKeyboardButton('Cancel', callback_data='CANCEL'))
    markup.add(button_1)
    return markup


async def start_processing():
    markup = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('✅OK', callback_data='PROCESSING')
    markup.add(InlineKeyboardButton('Cancel', callback_data='CANCEL'))
    markup.add(button_1)
    return markup



async def accept_usdt():
    markup = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('✅I paid', callback_data='KEYPRIMEUSDT')
    markup.add(InlineKeyboardButton('Cancel', callback_data='CANCEL'))
    markup.add(button_1)
    return markup

async def accept_BTC():
    markup = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('✅I paid', callback_data='KEYPRIMEBTC')
    markup.add(InlineKeyboardButton('Cancel', callback_data='CANCEL'))
    markup.add(button_1)
    return markup


async def check_pay_qiwi():
    markup = InlineKeyboardMarkup(row_width=2)
    button_1 = InlineKeyboardButton('Проверить платеж', callback_data='CHECK_PAY_QIWI:')
    markup.add(InlineKeyboardButton('Отмена', callback_data='CANCEL'))
    markup.add(button_1)
    return markup

async def exit():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Exit', callback_data='EXIT'))
    return markup

async def go_tochannel():
    markup = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('➡️ Go to channel', callback_data='GO_TO_CHANNEL')
    markup.add(button_1)
    markup.add(InlineKeyboardButton('💢 Exit', callback_data='EXIT'))
    return markup
    
async def bug_reports():
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('bugs', callback_data='BUG_REPORTS')
    markup.add(btn1)
    markup.add(InlineKeyboardButton('💢 Exit', callback_data='EXIT'))
    return markup

async def reviews():
    markup = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('➡️ Go to channel', callback_data='REVIEWS')
    markup.add(button_1)
    markup.add(InlineKeyboardButton('💢 Exit', callback_data='EXIT'))
    return markup

async def ddline():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton('💢 Exit', callback_data='EXIT'))
    return markup

async def feedbacks():
    markup = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('❓ Ask a question', callback_data='FEEDBACKSEC')
    markup.add(button_1)
    markup.add(InlineKeyboardButton('💢 Exit', callback_data='EXIT'))
    return markup


async def deladress():
    markup = InlineKeyboardMarkup(row_width=3)
    # basket = InlineKeyboardButton('🛒   view basket ', callback_data='')

    # markup.add(basket)
    markup.add(InlineKeyboardButton('💢 Exit', callback_data='EXIT'))
    return markup


async def counrty():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton('Английский', callback_data='ANGLY'),
        InlineKeyboardButton('Французский', callback_data='FRANCE'),
        InlineKeyboardButton('Итальянский', callback_data='ITALY'),
        InlineKeyboardButton('Словацкий', callback_data='SLOVAKIY'),
        InlineKeyboardButton('Австрийский', callback_data='AVSTRY')
    )
    return markup