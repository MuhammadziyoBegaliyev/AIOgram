from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
import states


async def start_command_answer(message: Message, bot : Bot):
    await message.answer("Assalomu aleykum botdan foydala olmasangiz /help buyrugini yuboring.")


async def help_command_answer(message: Message,bot: Bot):
    matn = """Botdan foydalanish:
    /new - yangi ariza yuborish
    /stop-joriy arizani bekor qilish
    """
    await message.answer(matn)

async def new_command_answer(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Menga ism-familyangizni yuboring: ")
    await state.set_state(states.newAriza.name)


async def stop_command_answer(message: Message, bot: Bot, state: FSMContext):
    this_state = await state.get_state()
    if this_state == "None":await message.answer("Bekor qilish uchun ariza mavjud emas!")
    else:
        await message.answer("Joriy ariza bekor qilindi !")
        await states.clear()


async def newAriza_name_answer(message: Message, bot: Bot, state: FSMContext):
    if len(message.text.split()) == 2:
        if not ("0" in  message.text or 
            "1" in message.text or 
            "2" in message.text or 
            "3" in message.text or 
            "4" in message.text or 
            "5" in message.text or 
            "6" in message.text or 
            "7" in message.text or 
            "8" in message.text or 
            "9" in message.text ):
            await state.update_data(name=message.text)
            await message.answer(f"Ism familya qabul qilindi. \n\n{message.text}")
            await message.answer("Menga yoshingizni yuboring: ")
            await state.set_state(states.newAriza.age)
        else : await message.answer("Ism-Familyada raqam qatnashishi mumkin emas!")
    else : await message.answer("Menga faqat ism familyangizni yuboring !")

async def newAriza_age_answer(message: Message, bot:Bot, state:FSMContext):
    if message.text.isdigit():
        if int(message.text) < 150 and int(message.text) > 7:
            await state.update_data(age=message.text)
            await message.answer(f"Yoshingiz qabul qilindi . \n\n{message.text}")
            await message.answer("Telefon raqamingizni kiriting: ")
            await state.set_state(states.newAriza.phone)
        elif int(message.text) > 150 and int(message.text) > 7 : await message.answer("Men 150 yoshdan oshgan odam ariza berayotganiga ishonmayman. ")
        else : await message.answer("Men 7 yoshdan kichiklarni qabul qilmayman.")
    else: await message.answer("Menga yoshingizni raqamlarda kiriting. ")

async def newAriza_phone_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(phone = message.text)
    await message.answer(f"Telefon Raqamingiz qabul qilindi . \n\n {message.text}")
    await message.answer("Kasbingiz nima?")
    await state.set_state(states.newAriza.job)


async def newAriza_job_answer(message: Message, bot: Bot , state: FSMContext):
    await state.update_data(job = message.text)
    await message.answer(f"Kasbingiz qabul qilindi. \n\n{message.text}")
    await message.answer("Maqsadingiz nima?")
    await state.set_state(states.newAriza.goal)

async def newAriza_goal_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(goal=message.text)
    await message.answer(f"Maqsadingiz qabul qilindi. \n\n{message.text}")
    data = await state.get_data()
    ariza = (f"Ariza beruvchi :{data.get('name')}\n"
             f"Yoshingiz : {data.get('age')}\n"
             f"Username: @{message.from_user.username}\n"
             f"Telefon raqami :{data.get('phone')}\n"
             f"kasbi: {data.get('job')}\n"
             f"Maqsadi : {message.text}\n")
    await message.answer(f"Arizani yuboraveremi? \n\n {ariza} Ha yoki /stop deb javob bering.")
    await state.set_state(states.newAriza.veryfy)

async def newAriza_verify_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text.lower() == 'ha':
        data = await state.get_data()
        ariza = (f"Ariza beruvchi :{data.get('name')}\n"
             f"Yoshingiz : {data.get('age')}\n"
             f"Username: @{message.from_user.username}\n"
             f"Telefon raqami :{data.get('phone')}\n"
             f"kasbi: {data.get('job')}\n"
             f"Maqsadi : {data.get('goal')}\n")
        
        await bot.send_message(6824528065, f"Yangi ariza :\n\n{ariza}")
        await message.answer("Arizangiz qabul qilindi.✅")
        await state.clear()
    else: await message.answer("yo menga ha deng yoki /stop buyrugini bosing.")
