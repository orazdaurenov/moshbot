from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callbacks import frontend, backend, fullstack
from keyboards.inline.frontendList import frontEndCourses

coursesCategory = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Front-End', callback_data='frontend')],
        [
            InlineKeyboardButton(text='Backend', callback_data='backend')
        ],
        [
            InlineKeyboardButton(text='FullStack', callback_data='fullstack')
        ],
        [
            InlineKeyboardButton(
                text='Cerca', switch_inline_query_current_chat='')
        ],
        [
            InlineKeyboardButton(text='Condividi', switch_inline_query='Bravi')
        ],
    ],
)


# 2nd method of creating inline button

frontEnd = InlineKeyboardMarkup(row_width=1)
for key, value in frontEndCourses.items():
    frontEnd.insert(InlineKeyboardButton(
        text=key, callback_data=frontend.new(item_name=value)))
back_button = InlineKeyboardButton(text='Back', callback_data='cancel')
frontEnd.insert(back_button)
