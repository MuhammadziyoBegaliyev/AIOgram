from aiogram.types import Message
from aiogram import Bot
from keyboards_for10 import test_for_markup

async def start_command_reply(message: Message):
    await message.reply("Tugmalardan birini tanlang", reply_markup=test_for_markup)


async def get_contact_info(message: Message):
    contact_info = f"""
----------------
ism-familya: {message.contact.first_name}{message.contact.last_name}
----------------
user id:{message.contact.user_id}
----------------
telefon raqam:{message.contact.phone_number}
--------------

"""
    await message.reply('Kantakt qabul qilindi'+ contact_info)

async def get_locatio_info(message:Message):
    locatio_info= f"""
----------------
kenglik: {message.location.latitude}
----------------
uzunlik: {message.location.longitude}
----------------
"""
    await message.answer("Joylashuv imkoniyatlari:"+ locatio_info)