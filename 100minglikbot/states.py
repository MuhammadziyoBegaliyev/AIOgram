from aiogram.fsm.state import StatesGroup, State

class StartAriza(StatesGroup):
    name = State()
    age = State()
    phone = State()
    job = State()
    goal = State()
    verify = State()

    ### state qadamlarni belgilaydi , ketma ketlikda so`reydi 