from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon_ru import LEXICON_RU_MENU

async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command=com,
                   description=desc)
        for com, desc in LEXICON_RU_MENU.items()
    ]
    await  bot.set_my_commands(main_menu_commands)
