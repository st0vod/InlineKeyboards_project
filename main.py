import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from configs.config import load_config, Config
from keyboards.set_bot_menu import set_main_menu
from handlers.command_handlers import router_commands_handler

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] #%(levelname)-8s %(filename)s: %(lineno)d - %(name)s - %(message)s')
logger = logging.getLogger()


async def main():
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router_commands_handler)

    await set_main_menu(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
