from aiogram.types import Message
from aiogram import Bot

async def reklama_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in ("administrator", "creator"):
        return
    else:
        await message.delete()
        await message.answer(f"{message.from_user.full_name} REKLAMA TARQATMANG!!!❌")
        

    