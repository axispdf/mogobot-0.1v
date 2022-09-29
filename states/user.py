from aiogram.dispatcher.filters.state import State, StatesGroup


class settUser(StatesGroup):
    topUp = State()
    coupon = State()


class WithdrawState(StatesGroup):
    amount = State()
    address = State()


class SellCashCodeState(StatesGroup):
    data = State()



class FormCoinUSDT(StatesGroup):
    USDT = State()
    amount = State()
    

class FormCoinBTC(StatesGroup):
    BTC = State()
    amount = State()


class Form(StatesGroup):
    qiwi = State()


class Report(StatesGroup):
    text = State()
    img = State()


class DAdress(StatesGroup):
    adress = State()