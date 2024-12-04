from aiogram import Bot , Dispatcher ,F
from asyncio import run

dp = Dispatcher()

async def startup_answer(bot:Bot):
    await bot.send_message(6824528065, "Bot ishga tushdi ✅")


async def shutdown_answer(bot:Bot):
    await bot.send_message(6824528065, "Bot ishdan to`xtadi ❌")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    bot = Bot("7682918479:AAFIwfOI81ESlA1-KkZDyiueKX3_YrgL2Ik")