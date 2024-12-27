# from aiogram.types import Message
# from aiogram import Bot 
# from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext

# async def help_command_answer(message: Message, bot: Bot):
#     text = """ 
#     📢 Diqqat! Diqqat! Diqqat!
# 🏆 “Yil tanlovi — 2024”da ishtirok eting!!!  
    
# 🥇Chortoq tumanida taʼlim va yoshlar uchun xizmat qilgan hamda Prezidentning odilona siyosatini qoʻllab-quvvatlagan yilning eng faol maktab direktorlariga ovoz bering!
    
# 🕒 Soʻrovnoma muddati:
# Soʻrovnoma 2024-yil 26-dekabr, soat 22:00 gacha davom etadi.
    
# 🎉 Mukofotlar:
# Gʻolib deb topilgan 3 nafar maktab direktorlariga maxsus qimmatbaho sovgʻalar  va sertifikat bilan taqdirlanadi.
    
# 👉 OVOZ BERISH (@Salom_0298) Sizning fikringiz biz uchun muhim!
    
# 🤝Ushbu soʻrovnoma Chortoq tuman maktabgacha va maktab ta'limi bo'limi hamda MegaZiyo (@Salom_0298) hamkorligida boʻlib oʻtmoqda!
#     """
#     await message.answer(text)
# ###



from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

# Global o'zgaruvchilarni saqlash uchun
vote_count_1 = 0
vote_count_2 = 0

# Foydalanuvchiga yordam matnini yuborish
async def help_command_answer(message: Message, bot: Bot):
    text = """ 
    📢 Diqqat! Diqqat! Diqqat!
🏆 “Yil tanlovi — 2024”da ishtirok eting!!!  
    
🥇Chortoq tumanida taʼlim va yoshlar uchun xizmat qilgan hamda Prezidentning odilona siyosatini qoʻllab-quvvatlagan yilning eng faol maktab direktorlariga ovoz bering!
    
🕒 Soʻrovnoma muddati:
Soʻrovnoma 2024-yil 26-dekabr, soat 22:00 gacha davom etadi.
    
🎉 Mukofotlar:
Gʻolib deb topilgan 3 nafar maktab direktorlariga maxsus qimmatbaho sovgʻalar va sertifikat bilan taqdirlanadi.
    
👉 OVOZ BERISH (@Salom_0298) Sizning fikringiz biz uchun muhim!
    
🤝Ushbu soʻrovnoma Chortoq tuman maktabgacha va maktab ta'limi bo'limi hamda MegaZiyo (@Salom_0298) hamkorligida boʻlib oʻtmoqda!
    """
    
    # Inline klaviaturani yaratish
    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Tugma 1", callback_data="vote_1"),
                InlineKeyboardButton(text="Tugma 2", callback_data="vote_2"),
            ]
        ]
    )

    # Foydalanuvchiga xabar yuborish
    await message.answer(text, reply_markup=inline_keyboard)


    # Callback queryni qayta ishlash
    async def process_vote(callback_query: CallbackQuery, bot: Bot, state: FSMContext):
        global vote_count_1, vote_count_2  # Global o'zgaruvchidan foydalanish
        print("1-tugma")

        # Ovoz berish tugmasi bosilganda qiymatni yangilash
        if callback_query.data == "vote_1":
            vote_count_1 += 1
            await bot.answer_callback_query(callback_query.id, text="Tugma 1 uchun ovoz berildi!")
        elif callback_query.data == "vote_2":
            vote_count_2 += 1
            await bot.answer_callback_query(callback_query.id, text="Tugma 2 uchun ovoz berildi!")

        # Tugmalarni yangilash
        keyboard = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(f"1. Ovoz berish {vote_count_1}", callback_data="vote_1")
        button2 = InlineKeyboardButton(f"2. Ovoz berish {vote_count_2}", callback_data="vote_2")
        
        keyboard.add(button1, button2)
        
        # Callback queryni yangilash
        await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text=callback_query.message.text,
            reply_markup=keyboard
        )


