from aiogram.types import Message, ChatPermissions
from aiogram import Bot
from datetime import timedelta, datetime

async def new_chat_members_answer(message: Message):
    for new_chat_member in message.new_chat_members:
        await message.answer(f"Hi, {new_chat_member.full_name}")
        await message.delete()

async def left_chat_member_answer(message: Message):
    await message.answer(f"By , by , {message.left_chat_member.full_name}")
    await message.delete()

async def mute_member_answer(message: Message):
    user_id = message.reply_to_message.from_user.id
    permissions = ChatPermissions(can_send_messages=False) 
    await message.chat.restrict(user_id, permissions )
    await message.answer(f"{message.reply_to_message.from_user.mention_html()} yozishdan maxrum qilindi !",parse_mode="HTML")

async def unmute_member_answer(message: Message):
        
        user_id = message.reply_to_message.from_user.id
        permissions = ChatPermissions(can_send_messages=True) 
        await message.chat.restrict(user_id, permissions )
        await message.answer(f"{message.reply_to_message.from_user.mention_html()} yozish imkoniyati berildi  !",parse_mode="HTML")

async def ban_member_answer(message: Message):
        user_id = message.reply_to_message.from_user.id
        await message.chat.ban_sender_chat(user_id)
        await message.answer(f"{message.reply_to_message.from_user.mention_html()} Guruxdan xaydaldi !",parse_mode="HTML")

async def unban_member_answer(message: Message):
        user_id = message.reply_to_message.from_user.id
        await message.chat.unban_sender_chat(user_id)
        await message.answer(f"{message.reply_to_message.from_user.mention_html()} Guruxga qaytdingiz",parse_mode="HTML")
