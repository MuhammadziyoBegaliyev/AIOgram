from aiogram import Router, F
from aiogram.filters import and_f, Command
from . import new_member
from . import left_chat_member
from . import ban
from . import mute

router = Router()

router.message.register(new_member.new_member_answer, F.new_chat_members)
router.message.register(left_chat_member.left_chat_member_answer, F.left_chat_member)
router.message.register(ban.ban_command_answer, F.text == "/ban")
router.message.register(ban.unban_command_answer, F.text == "/unban")
router.message.register(mute.mute_command_answer, F.text == "/mute")
router.message.register(mute.unmute_command_answer, F.text == "/unmute")