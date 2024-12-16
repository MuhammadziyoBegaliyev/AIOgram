from aiogram import Router
from aiogram.filters import CommandStart
import user 


router = Router()
router.include_router(user.command_start_answer, CommandStart())