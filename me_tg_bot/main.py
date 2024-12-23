from aiogram import Bot, Dispatcher 
from asyncio import run 
from aiogram.types import BotCommand 
from aiogram.filters import Command
import function 
import states


dp = Dispatcher()



async def startup_answer(bot:Bot):
    await bot.send_message(6824528065, "Bot ishga tushdi ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(6824528065, "Bo`t ishdan to`qtadi❌")



async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    dp.message.register(function.start_command_answer, Command("start",prefix="/!"))
    dp.message.register(function.help_command_answer,Command("help", prefix='/!'))
    dp.message.register(function.phonenum_command_answer,Command('phonenum',prefix='/!'))
    dp.message.register(function.new_command_answer,Command("Boglanish"))
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
        BotCommand(command = "/start", description="Botni ishga tushurush"),
        BotCommand(command="/return", description="Arizani bekor qilish"),
        BotCommand(command='/help', description="Bo`tdan foydalanishda yordam!"),
        BotCommand(command='/phone_num', description="Menga aloqaga chiqmoqchi bo`lsangiz!")

    ])
    await dp.start_polling(bot ,polling_timeout=1)


run(start())



