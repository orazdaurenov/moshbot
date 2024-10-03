from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from keyboards.inline.courseButton import courses
from loader import dp


@dp.message_handler(Text('📚 Courses'))
async def python_course(msg: Message):
    await msg.answer('Choose a course that you want', reply_markup=courses)
