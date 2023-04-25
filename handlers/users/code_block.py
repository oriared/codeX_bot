from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from states.states import FSMInterpreter
from loader import dp


@dp.message_handler(Text(startswith=(
                                     '$    ', 'for ', 'while ', 'if ', 'elif ',
                                     'else:', 'try:', 'except ', 'except:',
                                     'class ', 'def ', 'with '
                                    )),
                    state=FSMInterpreter.code)
async def code_block(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['current_code'] += message.text.lstrip('$') + '\n'
