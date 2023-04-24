from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMInterpretator(StatesGroup):
    code = State()
    fill_input = State()
    
    @staticmethod
    async def reset_state(state):
        async with state.proxy() as data:
            data['code'] = ''
            data['current_code'] = ''
            data['input'] = ''
            data['current_inputs'] = ''
            data['number_of_current_inputs'] = 0
            data['output_lenght'] = 0

            await FSMInterpretator.code.set()
