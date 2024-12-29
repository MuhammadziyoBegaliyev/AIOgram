
from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram.types import BotCommand, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import function
import callback_function
import states


dp = Dispatcher()

# Kanal username yoki ID
CHANNEL_ID = "@deltaedu"

async def is_user_subscribed(bot: Bot, user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False

async def startup_answer(bot: Bot):
    await bot.send_message(1304863799, "Bot ishga tushdi ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(1304863799, "Bot ishdan to‘xtadi ❌")

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
        await message.answer("Assalomu alaykum! Botdan foydalanishni boshlashingiz mumkin ✅,\n /ovoz - ovoz berish uchun📊 \n /ariza - ariza berish yoki shikoyat uchun📑 ")

@dp.callback_query(lambda call: call.data == "check_subscription")
async def check_subscription_callback(call, bot: Bot):
    user_id = call.from_user.id
    is_subscribed = await is_user_subscribed(bot, user_id)

    if is_subscribed:
        await call.message.edit_text("Rahmat! Siz kanalga obuna bo'ldingiz ✅ ,\n /ovoz - ovoz berish uchun📊 \n /ariza - ariza berish yoki shikoyat uchun📑 ")
    else:
        await call.answer("Siz hali ham obuna bo'lmagansiz ❌", show_alert=True)

# Botni ishga tushirish
async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    dp.message.register(function.help_command_answer1, Command("ovoz"))
    dp.callback_query.register(callback_function.process_vote,lambda c: c.data in ['vote_1', 'vote_2'])
    dp.message.register(function.help_command_answer1,Command("ovoz"))
    dp.message.register(function.help_command_answer, Command("ariza"))
    dp.message.register(function.phonenum_command_answer, Command("phonenum"))
    dp.message.register(function.new_command_answer, Command("Boglanish"))
    dp.message.register(function.stop_command_answer, Command("return"))
    dp.message.register(function.phonenum_command_answer, Command("phone_num"))
    dp.message.register(function.StartAriza_name_answer, states.StartAriza.name)
    dp.message.register(function.StartAriza_age_answer, states.StartAriza.age)
    dp.message.register(function.StartAriza_phone_answer, states.StartAriza.phone)
    dp.message.register(function.StartAriza_job_answer, states.StartAriza.job)
    dp.message.register(function.StartAriza_goal_answer, states.StartAriza.goal)
    dp.message.register(function.StartAriza_verify_answer, states.StartAriza.verify)

    bot = Bot("7825114169:AAFdETvvJXGOdbwI_33LWZNEVH7BU9x-5gY")
    await bot.set_my_commands([
        BotCommand(command="/start", description="Botni ishga tushurush"),
        BotCommand(command="/return", description="Arizani bekor qilish"),
        BotCommand(command="/ariza", description="Botdan foydalanishda yordam!"),
        BotCommand(command="/phone_num", description="Aloqaga chiqmoqchi bo‘lsangiz!")
    ])
    await dp.start_polling(bot, polling_timeout=1)

run(start())
