from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from aiogram.types import Message

class SubscriptionMiddleware(BaseMiddleware):
    async def __call__(self, 
                       handler: Callable[[Message, Dict[str, Any]],Awaitable[Any]],
                       event :Message,
                       data: Dict[str,Any]
                       )-> Any:
        channels = [
            "-1002236343456"
        ]
        channel_statuses = []
        for channel in channels:
            status = await event.bot.get_chat_member(
                chat_id =channel,
                user_id=event.from_user.id
            )
            channel_statuses.append(status.status)
            if "left" in channel_statuses:
                await event.answer(
                    text="Iltimos, batcha kanalga obuna bo`ling!"
                )
            else:
                return await handler(event,data)