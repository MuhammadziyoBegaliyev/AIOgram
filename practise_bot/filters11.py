from typing import Any
from aiogram.filters import Filter
from aiogram.types import Message
from aiogram import Bot
from data import CHANEL_ID


class CheckSubChannel(Filter):
    async def __call__(self, message: Message, bot: Bot):
        user_status = await bot.get_chat_member(CHANEL_ID, message.from_user.id)
        if user_status.status in ['member', 'administrator', 'creator']:
            return False
        else :
            return True