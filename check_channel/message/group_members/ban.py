from aiogram.types import Message
from aiogram import Bot

async def ban_command_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in ("administrator", "creator"):
        if message.reply_to_message:
            ban_user = message.reply_to_message.from_user
            await message.chat.ban(ban_user.id)
            await message.answer(f"{ban_user.full_name} Guruxdan bloklandi❌")
        else:
            await message.answer("Kimnidir bloklashim uchun uning xabariga reply qiling.")
    else: 
        await message.answer("Siz kimnidir bloklash uchun guruxda admin bo`lishingiz kerak ")


async def unban_command_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id) 
    if user.status in ("administrator", "creator"):
        if message.reply_to_message:
            ban_user = message.reply_to_message.from_user
            await message.chat.unban(ban_user.id)
            await message.answer(f"{ban_user.full_name} Blokdan ochildi✅")
        else:
            await message.answer("Kimnidir blokdan ochishimiz uchun xabar yuborishi kerak!")
    else:
        await message.answer("Siz kimnidur blokdan ochishingiz uchun asmin bo`lishingiz kerak")
    