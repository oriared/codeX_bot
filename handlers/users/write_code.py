from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from services.interpreter import execute_current_code
from states.states import FSMInterpreter


@dp.message_handler(state=FSMInterpreter.code)
async def write_code(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['current_code'] += message.text.lstrip('$') + '\n'
        inp: int = data['current_code'].count('input(')
        if inp:
            data['number_of_current_inputs'] = inp
            await FSMInterpreter.fill_input.set()
            await message.answer(text='####  ВВЕДИТЕ INPUT (один '
                                      'input в одном сообщении)  ####')
        else:
            await execute_current_code(data)
            if data['answer_to_user']:
                await message.answer(text=data['answer_to_user'])
