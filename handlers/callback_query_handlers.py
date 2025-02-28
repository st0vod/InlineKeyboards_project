from aiogram import Router, F
from aiogram.types import CallbackQuery

router_query = Router()


@router_query.callback_query(F.data == 'callback_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 1',
            reply_markup=callback.message.reply_markup)
    else:
        await callback.answer(text='Так работает callback.answer() с атрибутами text и show_alert=True',
                              show_alert=True)


@router_query.callback_query(F.data == 'callback_button_2_pressed')
async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 2',
            reply_markup=callback.message.reply_markup)
    else:
        await callback.answer(text='так работает callback.answer() с одним атрибутом text')


@router_query.callback_query(F.data.in_(list(map(str, range(1, 11)))))
async def process_button_i_press(callback: CallbackQuery):
    if callback.message.text != f'Это кнопка {callback.data}':
        await callback.message.edit_text(
            text=f'Это кнопка {callback.data}',
            reply_markup=callback.message.reply_markup)
    else:
        await callback.answer(text='Эта кнопка уже нажата')