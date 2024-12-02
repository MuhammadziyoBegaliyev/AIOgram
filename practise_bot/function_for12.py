from aiogram.types import Message
import keyboards_for12


async def echo(message: Message):
    await message.copy_to(message.chat.id, reply_markup=keyboards_for12.builder)