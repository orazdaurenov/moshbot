from aiogram.types import Message, CallbackQuery
from keyboards.inline.courseButton import coursesCategory, frontEnd
from loader import dp


@dp.message_handler(text_contains='Categories')
async def python_course(msg: Message):
    await msg.answer('What stack do you want to take up ?', reply_markup=coursesCategory)


@dp.callback_query_handler(text='frontend')
async def frontend(call: CallbackQuery):
    await call.message.answer('Choose your frontend courses', reply_markup=frontEnd)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='cancel')
async def back_btn(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('What stack do you want to take up ?', reply_markup=coursesCategory)
