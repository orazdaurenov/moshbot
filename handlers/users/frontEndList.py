from aiogram.types import CallbackQuery
from keyboards.inline.courseButton import frontEnd
from loader import dp


@dp.callback_query_handler(text_contains='frontend')
async def frontEndList(call: CallbackQuery):
    await call.message.answer('FrontEnd Courses', reply_markup=frontEnd)
    await call.answer(cache_time=60)
