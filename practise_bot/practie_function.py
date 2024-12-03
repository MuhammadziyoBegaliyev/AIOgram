from aiogram.types import Message

import practice_keyboard
async def echo(message: Message):
    await message.answer(text="kanalga azo bo`ling", reply_markup=practice_keyboard.inline_markup)