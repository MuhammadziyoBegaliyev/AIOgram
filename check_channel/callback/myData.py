from aiogram.types import CallbackQuery
from filter_for_callback.callback_data import MyFilter

async def myFunc(query: CallbackQuery, callback_data: MyFilter):
    await query.answer(text=f"Chat_id: {callback_data.chat_id}\nUser_id: {callback_data.user_id}", show_alert=True)