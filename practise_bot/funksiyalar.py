from aiogram import Bot
from aiogram.types import Message , ReplyKeyboardRemove
from keyboards import biror_bir_tugmalar

async def echo(message: Message, bot:Bot):
    await message.copy_to(message.chat.id)

async def qandaydur_answer(message: Message):   
    await message.answer("Qandeydur javob", reply_markup=biror_bir_tugmalar)

async def cancel_markup(message: Message):
    await message.answer("Markup tozalandi!", reply_markup=ReplyKeyboardRemove())