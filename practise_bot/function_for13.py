from aiogram.types import Message

import keyboards_for13

async def echo(message : Message):
    await message.copy_to(message.chat.id, reply_markup=keyboards_for13.inline_markup)