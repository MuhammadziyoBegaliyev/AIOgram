from aiogram.types import Message

async def get_channel_id_answer(message :Message):
    await message.answer(f"Kanal ID: {message.forward_from_chat.id}")

async def echo(message: Message):
    await message.copy_to(message.chat.id)
    
async def sub_channel_answer(message: Message):
    invite_link ="https://t.me/+8sEpkq3R4P84ZjVi"
    await message.answer(f"Kanalga obuna bo`lish. <a href='{invite_link}'>LINK</a>", parse_mode="HTML")