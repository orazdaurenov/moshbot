from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

courses = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Python Projects for Beginners',
                                 url='https://codewithmosh.com/p/python-projects-for-beginners')
        ],
    ],
)
