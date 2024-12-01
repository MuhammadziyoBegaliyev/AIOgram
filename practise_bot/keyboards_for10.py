from aiogram.types import ReplyKeyboardMarkup ,KeyboardButton

test_for_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Kantak yuborish', request_contact=True),
            KeyboardButton(text='Joylashuvni yuborish', request_location=True)
        ]
    ],
    resize_keyboard=True,
    is_persistent=True,
    input_field_placeholder="Tugmalardan birini tanlang."
)