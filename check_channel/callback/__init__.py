from aiogram import Router , F
from . import myData
import filter_for_callback

router = Router()
router.callback_query.register(myData.myFunc, filter_for_callback.callback_data.MyFilter.filter())