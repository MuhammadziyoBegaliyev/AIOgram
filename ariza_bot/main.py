from aiogram import Bot , Dispatcher
from asyncio import run 
from aiogram.types import BotCommand
from aiogram.filters import Command

import funksiya
from states import newAriza
dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(6824528065,  "Bot ishga tushurildi! ✅")


async def shutdown_answer(bot: Bot):
    await bot.send_message(6824528065,  "Bot To`xtatildi! ❌")

async def start():
    dp.startup.register(startup_answer)
    dp.message.register(funksiya.start_command_answer, Command("start",prefix="/!"))
    dp.message.register(funksiya.help_command_answer,Command("help"))
    dp.message.register(funksiya.new_command_answer,Command("new"))
    dp.message.register(funksiya.stop_command_answer, Command("stop"))
    dp.message.register(funksiya.newAriza_name_answer, newAriza.name)
    dp.message.register(funksiya.newAriza_age_answer, newAriza.age)
    dp.message.register(funksiya.newAriza_phone_answer, newAriza.phone)
    dp.message.register(funksiya.newAriza_phone_answer, newAriza.phone)
    dp.message.register(funksiya.newAriza_job_answer, newAriza.job)
    dp.message.register(funksiya.newAriza_goal_answer, newAriza.goal)
    dp.message.register(funksiya.newAriza_verify_answer, newAriza.veryfy)



    
    dp.shutdown.register(shutdown_answer)
    bot = Bot("7682918479:AAFIwfOI81ESlA1-KkZDyiueKX3_YrgL2Ik")
    
    await bot.set_my_commands([
        BotCommand(command="/new", description="yangi ariza yuborish"),
        BotCommand(command="/stop",description="Arizani bekor qilish"),
        BotCommand(command="/help",description="Bo`tdan foydalaninshda yordam ")
    ])


    await dp.start_polling(bot, polling_timeout=1)


run(start())
