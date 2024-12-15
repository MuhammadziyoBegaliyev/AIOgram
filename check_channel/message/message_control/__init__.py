from aiogram import Router, F
import filters.reklama_filter
from . import reklama
from . import can_sent
import filters


router = Router()


router.message.register(reklama.reklama_answer, filters.reklama_filter.IsReklama())
router.message.register(can_sent.on_command_answer, F.text == "/on")
router.message.register(can_sent.off_command_answer, F.text == "/off")

