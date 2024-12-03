from aiogram.types import Message

import keyboards_for14

async def echo(message:Message):
    await message.copy_to(message.chat.id, reply_markup=keyboards_for14.inline_builder)