from aiogram import types
from aiogram.dispatcher import FSMContext

from services.interpreter import execute_current_code
from states.states import FSMInterpreter
from loader import dp


@dp.message_handler(state=FSMInterpreter.fill_input)
async def fill_input(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['current_inputs'] += message.text.lstrip('$') + '\n'
        data['number_of_current_inputs'] -= 1
        
        if data['number_of_current_inputs'] > 0:
            await message.answer(text='#### ВВЕДИТЕ СЛЕДУЮЩИЙ INPUT ####')
        else:
            await FSMInterpreter.code.set()
            await execute_current_code(data)
            if data['answer_to_user']:
                await message.answer(text=data['answer_to_user'])
