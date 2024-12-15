from aiogram.types import Message

async def left_chat_member_answer(message: Message):
    left_member = message.left_chat_member
    await message.delete()
    await message.answer(f"Xayr, {left_member.full_name}!")