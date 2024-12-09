import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties # type: ignore


from config import load_config # type: ignore
from src.infrastructure.database import create_pool, make_connection_string # type: ignore

dp = Dispatcher()


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    config = load_config()
    bot = Bot(token=config.tgbot.token, default=DefaultBotProperties(parse_mode="HTML"))
    pool = create_pool(url=make_connection_string(config))
    middlewares.setup(dp, pool=pool)
    handlers.setup(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())