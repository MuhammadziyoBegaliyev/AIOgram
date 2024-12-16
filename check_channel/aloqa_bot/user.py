from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender
from asyncio import sleep


async def command_start_answer(message: Message):
    async with ChatActionSender.typing(message.from_user.id, bot):
        await sleep(2)
        await message.answer("Assalomu aleykum")