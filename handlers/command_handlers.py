from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU_MENU
from keyboards.inline_keyboard import keyboard_inline


router_commands_handler = Router()

@router_commands_handler.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU_MENU[message.text],
                         reply_markup=keyboard_inline

    )