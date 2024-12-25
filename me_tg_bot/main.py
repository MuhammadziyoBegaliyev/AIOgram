# from aiogram import Bot, Dispatcher 
# from asyncio import run 
# from aiogram.types import BotCommand 
# from aiogram.filters import Command
# import function 
# import states


# dp = Dispatcher()



# async def startup_answer(bot:Bot):
#     await bot.send_message(6824528065, "Bot ishga tushdi ✅")

# async def shutdown_answer(bot: Bot):
#     await bot.send_message(6824528065, "Bo`t ishdan to`qtadi❌")



# async def start():
#     dp.startup.register(startup_answer)
#     dp.shutdown.register(shutdown_answer)
#     dp.message.register(function.start_command_answer, Command("start",prefix="/!"))
#     dp.message.register(function.help_command_answer,Command("help", prefix='/!'))
#     dp.message.register(function.phonenum_command_answer,Command('phonenum',prefix='/!'))
#     dp.message.register(function.new_command_answer,Command("Boglanish"))
#     dp.message.register(function.stop_command_answer, Command("return"))
#     dp.message.register(function.phonenum_command_answer, Command("phone_num"))
#     dp.message.register(function.StartAriza_name_answer, states.StartAriza.name)
#     dp.message.register(function.StartAriza_age_answer, states.StartAriza.age)
#     dp.message.register(function.StartAriza_phone_answer, states.StartAriza.phone)
#     dp.message.register(function.StartAriza_job_answer, states.StartAriza.job)
#     dp.message.register(function.StartAriza_goal_answer, states.StartAriza.goal)
#     dp.message.register(function.StartAriza_verify_answer, states.StartAriza.verify)


#     bot = Bot("7880510782:AAFbrrMbdQFLoc_EriE3P_6KxKZoRm_XfoQ")

#     await bot.set_my_commands([
#         BotCommand(command = "/start", description="Botni ishga tushurush"),
#         BotCommand(command="/return", description="Arizani bekor qilish"),
#         BotCommand(command='/help', description="Bo`tdan foydalanishda yordam!"),
#         BotCommand(command='/phone_num', description="Menga aloqaga chiqmoqchi bo`lsangiz!")

#     ])
#     await dp.start_polling(bot ,polling_timeout=1)


# run(start())



####


from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram.types import BotCommand, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import function
import states

dp = Dispatcher()

# Kanal username yoki ID
CHANNEL_ID = "@https://t.me/formlivechannel_2025"

async def is_user_subscribed(bot: Bot, user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False

async def startup_answer(bot: Bot):
    await bot.send_message(6824528065, "Bot ishga tushdi ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(6824528065, "Bo`t ishdan to`qtadi❌")

async def check_subscription(message, bot: Bot):
    user_id = message.from_user.id
    is_subscribed = await is_user_subscribed(bot, user_id)

    if not is_subscribed:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="📢 Kanalga obuna bo'lish", url=f"{CHANNEL_ID[1:]}")
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

async def subscription_middleware(handler, message, bot: Bot):
    is_subscribed = await check_subscription(message, bot)
    if is_subscribed:
        await handler(message)

# Obunani tekshirish uchun callback qo'llash
@dp.callback_query(lambda call: call.data == "check_subscription")
async def check_subscription_callback(call, bot: Bot):
    user_id = call.from_user.id
    is_subscribed = await is_user_subscribed(bot, user_id)

    if not is_subscribed:
        await call.message.edit_text("Rahmat! Siz kanalga obuna bo'ldingiz ✅")
    else:
        await call.answer("Siz hali ham obuna bo'lmadingiz ❌", show_alert=True)

# Botni ishga tushirish
async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    # Majburiy obunani tekshirishni middleware sifatida qo'shish
    dp.message.middleware(lambda handler, message, bot: subscription_middleware(handler, message, bot))

    # Buyruqlarni ro'yxatga olish
    dp.message.register(function.start_command_answer, Command("start", prefix="/!"))
    dp.message.register(function.help_command_answer, Command("help", prefix='/!'))
    dp.message.register(function.phonenum_command_answer, Command('phonenum', prefix='/!'))
    dp.message.register(function.new_command_answer, Command("Boglanish"))
    dp.message.register(function.stop_command_answer, Command("return"))
    dp.message.register(function.phonenum_command_answer, Command("phone_num"))
    dp.message.register(function.StartAriza_name_answer, states.StartAriza.name)
    dp.message.register(function.StartAriza_age_answer, states.StartAriza.age)
    dp.message.register(function.StartAriza_phone_answer, states.StartAriza.phone)
    dp.message.register(function.StartAriza_job_answer, states.StartAriza.job)
    dp.message.register(function.StartAriza_goal_answer, states.StartAriza.goal)
    dp.message.register(function.StartAriza_verify_answer, states.StartAriza.verify)

    bot = Bot("7880510782:AAFbrrMbdQFLoc_EriE3P_6KxKZoRm_XfoQ")

    await bot.set_my_commands([
        BotCommand(command="/start", description="Botni ishga tushurush"),
        BotCommand(command="/return", description="Arizani bekor qilish"),
        BotCommand(command="/help", description="Bo`tdan foydalanishda yordam!"),
        BotCommand(command="/phone_num", description="Menga aloqaga chiqmoqchi bo`lsangiz!")
    ])
    await dp.start_polling(bot, polling_timeout=1)

run(start())



