from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_markup = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Kanalga a`zo bo`ling",
            url="https://example.com"
        )
    ],
    [
        InlineKeyboardButton(
            text="✅ Tekshirish",
            callback_data="check_join",
        )
    ]
])