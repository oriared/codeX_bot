from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp


@dp.message_handler(CommandHelp(), state='*')
async def cmd_help(message: types.Message):
    await message.answer(text='Вы можете прислать как готовый скрипт, так и писать '
                         'код построчно прямо в этом чате. \nДля очистки памяти '
                         'интерпретатора отправьте команду /r.\nЕсли используете '
                         'функцию input(), не передавайте ей никаких '
                         'аргументов.\nУчтите, что мессенджер удаляет ведущие пробелы, '
                         'для корректной работы блоков if, for, while и прочих ставьте '
                         'знак $ в начале строки, начинающейся с пробелов. Если хотите '
                         'отправить пустую строку, отправьте знак $ либо используйте '
                         'команду /e (например, чтобы выполнился только что написанный '
                         'блок if).\n\nТекущая версия Python: 3.6.9')
