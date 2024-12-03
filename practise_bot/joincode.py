from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

channel_list = ['https://t.me/+nJOMMx6HmeQyYTZi', 'https://t.me/+8sEpkq3R4P84ZjVi']

def get_channels_ikb() -> InlineKeyboardMarkup:
    builder =InlineKeyboardBuilder()
    for channel in channel_list:
        builder.button(text="Follow",url= channel)
        builder.button(text="A`zo bo`ldim", callback_data="check_follow",switch_inline_query=True)
        builder.adjust(1)
        return builder.as_markup()