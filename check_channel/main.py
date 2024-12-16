from aiogram import Bot, Dispatcher, F, flags
from asyncio import run , create_task, sleep
import message
from datetime import datetime

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(6824528065,"Bot ishga tushdi✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(6824528065,"Bot ishdan to`qtadi❌")

async def vazifa(bot: Bot):
    async def sub():
        hozir = datetime.now()
        if hozir.hour == 23 and hozir.minute == 23:
            await bot.send_message(6824528065, "salom")

    while True:
        await sub()
        await sleep(10)

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    bot = Bot("7494144156:AAEge0yU6F8QZoKHOeC9JkTu2iP6NYbC7xw",parse_mode="HTML")
    create_task(vazifa(bot))
    await dp.start_polling(bot, polling_timeout=1)


run(start())