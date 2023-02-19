import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage as ms
from SudokuBot import sudoku_handler


bot = Bot(token="5856094549:AAEFnk5XCnRiNzfNudeDc0OeIJhq6pq5dS0", parse_mode="html")
dp = Dispatcher(bot, storage=ms())


async def throttled(*args, **kwargs):
    m = args[0]
    await m.answer("Do not flood, please ;) \nYou can use bot only once per second!")


@dp.message_handler(commands=['start', 'help'])
@dp.throttled(rate=1, on_throttled=throttled)
async def start_command_handler(message: Message):
    await message.reply("Send me image of sudoku, and I will try to solve it for you! \nTry and you will receive the solution in a few seconds!")


@dp.message_handler(content_types="photo")
@dp.throttled(key="photo_handler", on_throttled=throttled)
async def photo_handler(message: Message):
    if message.from_user.id != 5856094549:
        await message.reply("This bot is for @adjuna03 only! \nContact him to access this bot.")
    else:
        asyncio.create_task(sudoku_handler(message))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
