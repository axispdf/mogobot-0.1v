from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageCantBeDeleted
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loader import dp, bot


# Обработка всех колбэков которые потеряли стейты после перезапуска скрипта
@dp.callback_query_handler(text="...", state="*")
async def processing_missed_callback(call: CallbackQuery):
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='CANCEL', state='*')
@dp.message_handler(commands="cancel", state="*")
@dp.message_handler(Text(equals="cancel" or 'Cancel', ignore_case=True), state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Action canceled")


# Обработка всех колбэков которые потеряли стейты после перезапуска скрипта
@dp.callback_query_handler(state="*")
async def processing_missed_callback(call: CallbackQuery):
    print(call.data)
    try:
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    except MessageCantBeDeleted:
        pass
    await bot.send_message(call.from_user.id, "❌ *Data was not found due to script restart.\n"
                                              "♻ Perform the action again.*")


# Обработка всех неизвестных сообщений
@dp.message_handler()
async def processing_missed_messages(message: types.Message):
    await message.answer("♦ *Unknown command.*\n"
                         "▶ Enter /start")
