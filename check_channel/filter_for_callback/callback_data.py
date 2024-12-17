from aiogram.filters.callback_data import CallbackData

class MyFilter(CallbackData, prefix="my"):
    chat_id: str
    user_id: str