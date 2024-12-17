from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender
from asyncio import sleep
import asyncio
import keyboards

async def salomlash(message: Message):
    await message.answer("Salom",reply_markup=keyboards.inline.myFunc(message.chat.id, message.from_user.id))