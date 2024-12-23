from aiogram.types import Message
from aiogram import Bot 
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import states



async def start_command_answer(message:Message, bot: Bot):
    await message.answer("Assalomu aleykum , Botdan foydalanishni bilmasangiz /help buyrugini yuboring!")
    

async def help_command_answer(message: Message, bot: Bot):
    taxt = """ Bo`tdan foydalanish📱 :
    /Boglanish - Ariza yozishni boshlash📄
    /return - arizani bekor qilish❌
    /phone_num - Men bilan boglanish📞
    """
    await message.answer(taxt)

async def phonenum_command_answer(message: Message, bot: Bot):
    await message.answer("Men bilan boglanish uchun asosiy nomerlar \n +998901431051 \n +998941060109")


async def new_command_answer(message:Message, bot:Bot,state:FSMContext):
    await message.answer("Menga ism-familyangizni yuboring✍️")
    await state.set_state(states.StartAriza.name)

async def stop_command_answer(message: Message, bot: Bot, state: FSMContext):
    this_state = await state.get_state()
    if this_state == "None": await message.answer("Siz ariza yaratmadingiz😐")
    else:
        await message.answer("Ariza bekor qilindi 📝")
        await state.clear()

async def StartAriza_name_answer(message: Message, bot: Bot , state: FSMContext):
    if len(message.text.split()) == 2:
        if not ("0" in message.text or 
            "1" in message.text or 
            "2" in message.text or 
            "3" in message.text or 
            "4" in message.text or 
            "5" in message.text or 
            "6" in message.text or 
            "7" in message.text or 
            "8" in message.text or 
            "9" in message.text):
            await state.update_data(name=message.text)
            await message.answer(f"Ism-familya qabul qilindi✅ \n\n{message.text}")
            await message.answer("Menga yoshingizni yuboring.")
            await state.set_state(states.StartAriza.age)
        else: await message.answer("Ism-familyada raqam qatnashishi mumkin emas!")
    else: await message.answer("Menga faqat ism familyangizni yuboring")

async def StartAriza_age_answer(message: Message, bot : Bot, state: FSMContext):
    if message.text.isdigit():
        if int(message.text) < 150 and int(message.text) > 0 :
            await state.update_data(age=message.text)
            await message.answer(f"Yoshingiz qabul qilindi✅ \n\n {message.text}")
            await message.answer("Siz bilan boglanishimiz uchun telefon raqamingizni kiriting☎️")
            await state.set_state(states.StartAriza.phone) 
        elif int(message.text) >150 : await message.answer("Men 150 dan oshgan odam ariza berayotganiga ishonmayman.")
        else : await message.answer("Men 10 yoshdan kichik odam ariza berayotganiga ishonmayman")
    else : await message.answer("Menga yoshingizni raqamlarda kiriting.")


async def StartAriza_phone_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer(f"Telefon raqamingiz qabul qilindi. \n\n{message.text}")
    await message.answer("Kasbingiz nima?")
    await state.set_state(states.StartAriza.job)

async def StartAriza_job_answer(message: Message , bot: Bot , state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer(f"Kasbingiz qabul qilindi . \n\n{message.text}")
    await message.answer("Men bilan nima maqsadda boglanboqchisiz ?")
    await state.set_state(states.StartAriza.goal)

async def StartAriza_goal_answer(message: Message, bot : Bot, state:FSMContext):
    await state.update_data(goal=message.text)
    await message.answer(f"Maqsadingiz qabul qilindi \n\n {message.text}")
    data = await state.get_data()
    ariza = (f"Bog`lanuvchi :{data.get('name')}\n"
             f"Username: @{message.from_user.username}\n"
             f"Yoshi: {data.get('age')}\n"
             f"Telefon raqami: {data.get('phone')}\n"
             f"Kasbi : {data.get('job')}\n"
             f"Maqsadi : {data.get('goal')}\n"
             ) 
    await message.answer(f"Ma`lumotlaringizni yuboravereymi ?\n\n{ariza}\n\n Ha yoki /return dep javob bering ")
    await state.set_state(states.StartAriza.verify)

async def StartAriza_verify_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text.lower() == 'ha':
            data = await state.get_data()
            ariza = (f"Bog`lanuvchi :{data.get('name')}\n"
                    f"Username: @{message.from_user.username}\n"
                    f"Yoshi: {data.get('age')}\n"
                    f"Telefon raqami: {data.get('phone')}\n"
                    f"Kasbi : {data.get('job')}\n"
                    f"Maqsadi : {data.get('goal')}\n"
             ) 
            await bot.send_message(6824528065,f"Yangi Boglanuvchi topildi !\n\n {ariza}")
            await message.answer("Arizangiz qabul qilindi.✅")
            await state.clear()
    else: await message.answer(f"Yo menga ha deng yoki /return buyrug`ini yuboring.")