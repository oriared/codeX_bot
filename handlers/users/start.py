from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext


from loader import dp
from states.states import FSMInterpretator
from utils.lexicon import instructions


start_text = ('Приветствую.\nЭто бот-интерпретатор Python.\n'
              'Работает через API сайта https://codex.jaagrav.in/\n')


@dp.message_handler(CommandStart(), state=FSMInterpretator.all_states)
async def cmd_start(message: types.Message, state: FSMContext):
    await FSMInterpretator.reset_state(state)
    await message.answer(text=start_text + instructions)
