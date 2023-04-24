from typing import Optional
import requests

url = 'https://api.codex.jaagrav.in'

def execute_code(language: str, code: str, inp: str) -> tuple[str, str]:
    data: dict = dict(language=language, code=code, input=inp)
    response = requests.post(url, data).json()
    print(response)
    print()
    return response['output'], response['error']