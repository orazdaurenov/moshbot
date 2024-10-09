from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler(Text(contains='Subscribe'))
async def subscribe(msg: Message):
    await msg.answer('https://codewithmosh.com/p/all-access')
