from aiogram.types import Message



async def new_chat_members_answer(message: Message):
    for new_chat_member in message.new_chat_members:
        await message.answer(f"Hi , {new_chat_member.full_name}")
        await message.delete()

async def left_chat_member_answer(message: Message):
    await message.answer(f"By by , {message.left_chat_member.full_name}")
    await message.delete()

# async def get_info(message : Message):
#     await message.answer(
#         text=f"Chat ma`lumotlari :\n"
#              f"Chat turi : {message.chat.type}\n"
#              f"Chat nomi : {message.chat.title}\n"
#              f"Chat id : {message.chat.id}"
#     )