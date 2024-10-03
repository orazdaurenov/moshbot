from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.mainMenu import mainMenu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hey, {message.from_user.full_name}! Welcome to Mosh's Dev Community\n")
    await message.answer("Become the software engineer that companies love to hire", reply_markup=mainMenu)
