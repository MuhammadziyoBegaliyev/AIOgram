from aiogram import Bot, Dispatcher, F
from asyncio import run
import message

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(6824528065, "Bot ishga tushdi✅")

async def shutdown_answer(bot: Bot):    
    await bot.send_message(6824528065,"Bot ishdan toqtadi !")


async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    dp.include_router(message.router)
    bot = Bot("7980849345:AAFCC4Hb49niPJO6Lp7aY39Un3u5ZGlgz5E")
    await dp.start_polling(bot,polling_timeout=1)



run(start())    