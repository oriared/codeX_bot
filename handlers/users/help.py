from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp
from utils.lexicon import instructions


@dp.message_handler(CommandHelp(), state='*')
async def cmd_help(message: types.Message):
    await message.answer(text=instructions)
