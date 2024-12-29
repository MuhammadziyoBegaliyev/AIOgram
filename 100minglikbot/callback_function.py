from aiogram import Bot
from aiogram.types import CallbackQuery , InlineKeyboardButton , InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext


vote_count_1 = 0
vote_count_2 = 0

voted_users = set()

async def process_vote(callback_query: CallbackQuery, bot: Bot, state: FSMContext):
    global vote_count_1, vote_count_2
    user_id = callback_query.from_user.id

    if user_id in voted_users:
        await bot.answer_callback_query(callback_query.id, text="Siz allaqachon ovoz berdingiz!", show_alert=True)
        return

    voted_users.add(user_id)

    if callback_query.data == "vote_1":
        vote_count_1 += 1
        await bot.answer_callback_query(callback_query.id, text="Tugma 1 uchun ovoz berildi!") 
    elif callback_query.data == "vote_2":
        vote_count_2 += 1
        await bot.answer_callback_query(callback_query.id, text="Tugma 2 uchun ovoz berildi!")

    # Yangilangan klaviaturani qayta hosil qilish
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"Matematika : {vote_count_1} ovoz", callback_data="vote_1"),
                InlineKeyboardButton(text=f"Fizika : {vote_count_2} ovoz", callback_data="vote_2"),
            ]
        ]
    )

    await bot.edit_message_reply_markup(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=keyboard
    )



inline_markup = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ariza", callback_data="/ariza",),
        InlineKeyboardButton(text="OVOZ", callback_data="ovoz")
    ]
])