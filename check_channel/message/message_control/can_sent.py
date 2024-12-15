from aiogram.types import Message, ChatPermissions
from aiogram import Bot

async def on_command_answer(message: Message):
    permissions =ChatPermissions(can_send_messages=True)
    await message.chat.set_permissions(permissions)
    await message.answer(f"Guruxda xabar yuborish yopildi ")

async def off_command_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in ("administrator", "creator"):
        permissions = ChatPermissions(can_send_messages=False)
        await message.chat.set_permissions(permissions)
        await message.answer(f"Guruhga xabar yuborish cheklandi!")
    else:
        await message.answer("Siz guruhga xabar yuborishni cheklashingiz uchun guruh admini bo`lishingiz kerak ")
