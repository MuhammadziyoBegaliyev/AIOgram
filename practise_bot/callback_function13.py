from aiogram.types import CallbackQuery 
from aiogram import Bot

async def salom_action(callback_data : CallbackQuery, bot:Bot):
    await bot.answer_callback_query(callback_data.id,"Xabar yuborildi", show_alert=False)
    await callback_data.message.answer(text="Salom toy😂")
    await callback_data.answer("Xabar jo`natildi! ", show_alert= True)