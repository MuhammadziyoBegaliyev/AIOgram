from aiogram.types import Message, ChatPermissions
from aiogram import Bot

async def mute_command_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id) 
    if user.status in ("administrator", "creator"):
        if message.reply_to_message:
            user = message.reply_to_message.from_user
            permissions = ChatPermissions(can_send_messages=False)
            await message.chat.restrict(user.id, permissions)
            await message.answer(f"{user.full_name} endi xabar yoza  olmeydi❌")
        else:
            await message.answer("Kimnidur mute xolatiga tushirishni istaysizmi?")
    else:
        await message.answer("Siz kimnidir mute xolatiga tushurishingiz uchun admin bo`lishingiz kerak")



async def unmute_command_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id) 
    if user.status in ("administrator", "creator"):
        if message.reply_to_message:
            user = message.reply_to_message.from_user
            permissions = ChatPermissions(can_send_messages=True)
            await message.chat.restrict(user.id, permissions)
            await message.answer(f"{user.full_name} endi xabar yoza oladi✅")
        else:
            await message.answer("Kimnidur mute xolatiga tushirishni istaysizmi?")
    else:
        await message.answer("Siz kimnidir mute xolatiga tushurishingiz uchun admin bo`lishingiz kerak")