from aiogram import types
from filters.private_chat import IsPrivate
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hey, {message.from_user.full_name}! Welcome to Mosh's Dev Community\n")
    await message.answer("Become the software engineer that companies love to hire")
