from aiogram import types
from aiogram.dispatcher import FSMContext

from services.codex_api import execute_code
from states.states import FSMInterpretator
from loader import dp

@dp.message_handler(state=FSMInterpretator.all_states, commands=('e'))
async def empty_string(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['current_code'] += '\n'
        text, errors = execute_code('py', 
                                    data['code'] + data['current_code'], 
                                    data['input'] + data['current_inputs'])
        if text and len(text) > data['output_lenght'] + 1:
                await message.answer(text=text[data['output_lenght']:])
        if not errors:
            data['code'] += data['current_code']
            data['input'] += data['current_inputs']
            data['output_lenght'] = len(text)
        else:
            await message.answer(text=errors)
        data['current_code'] = ''
        data['current_inputs'] = ''