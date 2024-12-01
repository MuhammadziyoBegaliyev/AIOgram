from aiogram import Bot
from aiogram.types import Message

async def echo(message: Message, bot:Bot):
    await message.copy_to(message.chat.id)