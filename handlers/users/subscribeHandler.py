from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler(Text(contains='Subscribe'))
async def subscribe(msg: Message):
    await msg.answer('https://codewithmosh.com/p/all-access', reply_markup=ReplyKeyboardRemove)
