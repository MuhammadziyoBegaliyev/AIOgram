from aiogram import Bot , Dispatcher, types ,F
from asyncio import run 
from lesson3 import *
from aiogram.types import BotCommand
from aiogram.filters import Command
from states import *

dp = Dispatcher()
    
async def startup_answer(bot: Bot):
    await bot.send_message(6824528065, "Bot ishga tushdi!✅")


async def shutdown_answer(bot: Bot):
    await bot.send_message(6824528065, "Bot to`xtatildi!❌")



async def start():
    dp.startup.register(startup_answer)
    dp.message.register(start_answer, Command("start"))
    dp.message.register(help_answer, Command("help"))
    dp.message.register(sign_up_name, sign_up.name)
    dp.message.register(sign_up_age, sign_up.age)
    dp.message.register(get_user_info)
    dp.shutdown.register(shutdown_answer)
    bot = Bot("7682918479:AAFIwfOI81ESlA1-KkZDyiueKX3_YrgL2Ik")
    await bot.set_my_commands([
        BotCommand(command="/start",description="botni ishga tushurish"),
        BotCommand(command="/help", description="yordam olish")
    ])
    await dp.start_polling(bot, polling_timeout=1)


run(start())










