import logging

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU_MENU
from keyboards.inline_keyboard import keyboard_inline, keyboard_inline_callback
from functools import wraps

logger = logging.getLogger(name=__name__)


def id_info_decorator(func):
    """Декоратор выводит id пользователя, который совершил update"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        id = args[0].from_user.id
        logger.info('ID пользователя %s', id)
        return func(*args, **kwargs)

    return wrapper

router_commands_handler = Router()


@router_commands_handler.message(Command('url'))
@id_info_decorator
async def process_url_command(message: Message):
    await message.answer(text=LEXICON_RU_MENU[message.text],
                         reply_markup=keyboard_inline)


@router_commands_handler.message(Command('callback'))
@id_info_decorator
async def process_callback_command(message: Message):
    await message.answer(text=LEXICON_RU_MENU[message.text],
                         reply_markup=keyboard_inline_callback)
