from aiogram.types import Message

async def new_member_answer(message: Message):
    new_member = message.new_chat_members[0]
    await message.delete()
    await message.answer(f"Assalomu aleykum , {new_member.full_name} !")