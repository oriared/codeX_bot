from aiogram import types
from aiogram.dispatcher import FSMContext

from states.states import FSMInterpretator
from loader import dp


@dp.message_handler(state='*', commands=('r'))
async def cmd_start(message: types.Message, state: FSMContext):
    await FSMInterpretator.reset_state(state)
    await message.answer(text='Интерпретатор перезапущен')
