from aiogram import Bot, Dispatcher, F, flags
from asyncio import run 
from . import __init__

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(6824528065, "Bo`t ishga tushdi !✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(6824528065,"Bo`t ishdan to`qtadi❗️")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    dp.include_routers(__init__ .router)
    bot = Bot("7494144156:AAEge0yU6F8QZoKHOeC9JkTu2iP6NYbC7xw", parse_mode="HTML")
    await dp.start_polling(bot, polling_timeout=1)

run(start())