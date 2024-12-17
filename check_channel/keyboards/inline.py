from aiogram.utils.keyboard import InlineKeyboardBuilder
import filter_for_callback

def myFunc(chat_id, user_id):
    chat_id , user_id = str(chat_id), str(user_id)
    builder = InlineKeyboardBuilder()
    builder.button(text="Click", callback_data=filter_for_callback.callback_data.MyFilter(chat_id=chat_id, user_id=user_id).pack())
    return builder.as_markup()