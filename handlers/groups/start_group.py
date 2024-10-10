from aiogram import types
from filters.group_filter import IsGroup
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(IsGroup(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hey, {message.from_user.full_name}! Welcome to Mosh's Dev Group")
