from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


mainMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛎️ Subscribe'),
            KeyboardButton(text='📚 Categories'),
        ],
        [
            KeyboardButton(text='🛤️ Learning Path'),
            KeyboardButton(text='📢 Forum'),
            KeyboardButton(text='☎️ Contact'),
        ],
    ],
    resize_keyboard=True
)
