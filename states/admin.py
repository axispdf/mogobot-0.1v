from aiogram.dispatcher.filters.state import State, StatesGroup


class StatUserState(StatesGroup):
    u_id = State()


class settAdmin(StatesGroup):
    addCatalog = State()
    addSubCatalog = State()
    addProductName = State()
    addProductDescription = State()
    addProductPrice = State()
    addProductImg = State()
    addProductAdminPrice = State()
    addProductData = State()
    addCoupon = State()
    delItem = State()


class spam(StatesGroup):
    post = State()


class transaction(StatesGroup):
    address = State()
    amount = State()


class changeCoinbase(StatesGroup):
    token = State()


class SearchUser(StatesGroup):
    id = State()


class ChangeUser(StatesGroup):
    balance = State()


class SellAdminState(StatesGroup):
    amount = State()


