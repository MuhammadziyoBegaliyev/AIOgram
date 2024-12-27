
from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram.types import BotCommand, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import function

dp = Dispatcher()

# Kanal username yoki ID
CHANNEL_ID = "@Salom_0298"

async def is_user_subscribed(bot: Bot, user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False

async def startup_answer(bot: Bot):
    await bot.send_message(6824528065, "Bot ishga tushdi ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(6824528065, "Bot ishdan to‘xtadi ❌")

async def check_subscription(message, bot: Bot):
    user_id = message.from_user.id
    is_subscribed = await is_user_subscribed(bot, user_id)

    if not is_subscribed:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="📢 Kanalga obuna bo'lish", url=f"https://t.me/{CHANNEL_ID[1:]}")
                ],
                [
                    InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_subscription")
                ]
            ]
        )
        await message.answer(
            "❌ Siz kanalga obuna bo'lmagansiz. Iltimos, obuna bo'ling va qayta tekshiring.",
            reply_markup=keyboard
        )
        return False
    return True

@dp.message(Command("start"))
async def start_command_handler(message, bot: Bot):
    if await check_subscription(message, bot):
        await message.answer("Assalomu alaykum! Botdan foydalanishni boshlashingiz mumkin ✅, endi /help buyrugidan foydalanishni maslahat beraman ")

@dp.callback_query(lambda call: call.data == "check_subscription")
async def check_subscription_callback(call, bot: Bot):
    user_id = call.from_user.id
    is_subscribed = await is_user_subscribed(bot, user_id)

    if is_subscribed:
        await call.message.edit_text("Rahmat! Siz kanalga obuna bo'ldingiz ✅ , endi /help buyrugidan foydalanishni maslahat beraman ")
    else:
        await call.answer("Siz hali ham obuna bo'lmagansiz ❌", show_alert=True)

# Botni ishga tushirish
async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    dp.message.register(function.help_command_answer, Command("help"))
        # Command handler: help
    # Command handler: help
    dp.message(Command('help'), function.help_command_answer)
    
    # Callback handler: ovoz berish
    dp.callback_query(lambda c: c.data in ['vote_1', 'vote_2'], function.process_vote)

    bot = Bot("7937904548:AAGbgocGKSuRboN1dz3fnKfKJMCBLFwHCno")

    await dp.start_polling(bot, polling_timeout=1)

run(start())
