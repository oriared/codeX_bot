from aiogram import types
from aiogram.dispatcher import FSMContext

from services.codex_api import execute_code
from states.states import FSMInterpretator
from loader import dp

@dp.message_handler(state=FSMInterpretator.fill_input)
async def fill_input(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['current_inputs'] += message.text.lstrip('$') + '\n'
        data['number_of_current_inputs'] -= 1
        if data['number_of_current_inputs'] > 0:
            await message.answer(text='#### ВВЕДИТЕ СЛЕДУЮЩИЙ INPUT ####')
        else:
            await FSMInterpretator.code.set()
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
