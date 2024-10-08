from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Commandi: ",
            "/start - Avviare il Bot",
            "/help - Aiuto")

    await message.answer("\n".join(text))
