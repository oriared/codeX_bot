from aiohttp import ClientSession

from loader import bot


url = 'https://api.codex.jaagrav.in'


async def execute_code(code: str, inp: str) -> tuple[str, str]:
    data: dict = dict(language='py', code=code, input=inp)
    session: ClientSession = bot.get('codex_api_session')

    async with session.post(url, json=data) as resp:
        resp: dict = await resp.json()
        return resp['output'], resp['error']
