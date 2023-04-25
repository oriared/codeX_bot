from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMInterpreter(StatesGroup):
    code = State()
    fill_input = State()

    @staticmethod
    async def reset_state(state: State) -> None:
        async with state.proxy() as data:
            data['all_code'] = ''
            data['current_code'] = ''
            data['all_inputs'] = ''
            data['current_inputs'] = ''
            data['number_of_current_inputs'] = 0
            data['output_lenght'] = 0
            data['answer_to_user'] = ''

            await FSMInterpreter.code.set()
