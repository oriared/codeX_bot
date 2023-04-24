from aiogram import types
from aiogram.dispatcher import FSMContext

from services.codex_api import execute_code
from states.states import FSMInterpretator
from loader import dp

@dp.message_handler(state=FSMInterpretator.code)
async def write_code(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.startswith(('for ', 'while ', 'if ', 'elif ', 'else:',
                                    'try:', 'except ', 'except:', 'class ',
                                    'def ', 'with ')):
            data['current_code'] += message.text + '\n'
        elif message.text.startswith('$    '):
            data['current_code'] += message.text[1:] + '\n'
        else:
            data['current_code'] += message.text.lstrip('$') + '\n'
            inp = data['current_code'].count('input(')
            if inp:
                data['number_of_current_inputs'] = inp
                await FSMInterpretator.fill_input.set()
                await message.answer(text='####  ВВЕДИТЕ INPUT (один input в одном сообщении)  ####')
            else:
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