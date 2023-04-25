from .codex_api import execute_code


async def execute_current_code(data: dict) -> None:
    data['answer_to_user'] = ''
    text, errors = await execute_code(data['all_code'] + data['current_code'],
                                      data['all_inputs'] +
                                      data['current_inputs'])
    if len(text) > data['output_lenght'] + 1 or errors:
        data['answer_to_user'] = text[data['output_lenght']:] + errors
    if not errors:
        data['all_code'] += data['current_code']
        data['all_inputs'] += data['current_inputs']
        data['output_lenght'] = len(text)

    data['current_code'] = ''
    data['current_inputs'] = ''
