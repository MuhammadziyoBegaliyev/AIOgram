from aiogram import Router
from aiogram.filters import CommandStart
from . import user

from . import group_members
from . import message_control


router = Router()
router.message.register(user.salomlash)


# router.include_router(group_members.router)
# router.include_router(message_control.router)