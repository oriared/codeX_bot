from aiogram import types
from aiogram.dispatcher import FSMContext

from services.interpretator import execute_current_code
from states.states import FSMInterpretator
from loader import dp


@dp.message_handler(state=FSMInterpretator.all_states, commands=('e'))
async def empty_string(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['current_code'] += '\n'
        await execute_current_code(data)
        if data['answer_to_user']:
            await message.answer(text=data['answer_to_user'])
