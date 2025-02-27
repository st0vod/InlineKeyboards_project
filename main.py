import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from configs.config import load_config, Config
from keyboards.set_bot_menu import set_main_menu


logger = logging.getLogger()
logging.basicConfig(level='INFO')

async def main():
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    await set_main_menu(bot)
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
