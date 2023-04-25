from aiogram import types
from aiogram.dispatcher import FSMContext

from states.states import FSMInterpreter
from loader import dp


@dp.message_handler(state='*', commands=('r'))
async def cmd_start(message: types.Message, state: FSMContext):
    await FSMInterpreter.reset_state(state)
    await message.answer(text='Интерпретатор перезапущен')
