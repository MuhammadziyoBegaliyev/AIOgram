from aiogram import Bot, Dispatcher , F 
from asyncio import run 
import function_for14
import callback_function14
dp = Dispatcher()

async def startup_answer(bot : Bot):
    await bot.send_message(6824528065 , "Bot ishga tushdi ✅")

async def shutdown_answer(bot : Bot):
    await bot.send_message(6824528065 , "bot ishdan to`qtadi")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    dp.message.register(function_for14.echo)
    dp.callback_query.register(callback_function14.ok_answer, F.data == "ok")
    bot = Bot("7682918479:AAFIwfOI81ESlA1-KkZDyiueKX3_YrgL2Ik")
    await dp.start_polling(bot , polling_timeout=1)


run(start())