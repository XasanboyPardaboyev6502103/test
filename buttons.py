from aiogram.types import InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton


k_button=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="IT haqida"),KeyboardButton(text="IT kurslarimiz")]
    ],
    resize_keyboard=True
)


i_button=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Foundation",callback_data="foundation"),
            InlineKeyboardButton(text="Frontend",callback_data="frontend")
         ],
        [
            InlineKeyboardButton(text="Backend",callback_data="backend"),
            InlineKeyboardButton(text="Kiber Xavfsizlik",callback_data="kiber")
         ],


    ]
)