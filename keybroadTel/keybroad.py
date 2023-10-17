from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_client = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/Запуск Коня'),KeyboardButton(text='/список настроек')],
    ],
    resize_keyboard=True
)

