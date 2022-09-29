from aiogram.types import ReplyKeyboardMarkup

from config import button_profile, button_catalog, button_availability, button_feedbacksection
from database import db_select_admins


async def main_start(user):
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(button_catalog, button_profile).add(button_availability).add(button_feedbacksection)
    
    get_admin = db_select_admins(user)
    if get_admin:
        if get_admin[1] == 2:
            menu.add('Настройка продуктов', 'Сделать рассылку', 'Настройка каталога',
                     'Купоны', 'Сменить API', 'Перевести', 'Статистика', 'Пользователь')
    return menu