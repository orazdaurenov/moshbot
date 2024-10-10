from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.courseButton import frontEnd
from loader import dp


@dp.callback_query_handler(text_contains='frontend')
async def frontEndList(call: CallbackQuery):
    await call.message.answer('FrontEnd Courses', reply_markup=frontEnd, reply=ReplyKeyboardRemove())
    await call.answer(cache_time=60)
