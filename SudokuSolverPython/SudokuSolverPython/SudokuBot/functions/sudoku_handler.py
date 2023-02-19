import os, cv2
from datetime import datetime
from aiogram.types import *
from .solve_the_sudoku import solve_the_sudoku


async def sudoku_handler(message: Message):
    msg = await message.reply("Solving...")
    try:
        start_time = datetime.now().second

        image_path = f"./SudokuImages/{message.from_user.id} {message.photo[-1].file_unique_id}.{message.document}.png".replace(
            ".None", ""
        )

        await message.photo[-1].download(destination_file=image_path)

        print("Solving sudoku")
        result = solve_the_sudoku(
            image=image_path, model="./SudokuBot/models/DigitalRecognitionOCR.h5"
        )
        print("Solved sudoku")
        cv2.imwrite(image_path, result)

        end_time = datetime.now().second
        duration = end_time - start_time

        await msg.delete()
        await message.reply_photo(
            InputFile(image_path),
            caption=f"Done! \nEasy-peasy lemon squeezy! \n\nSolved in {duration} seconds by @solve_sudoku_bot",
        )
        os.remove(image_path)
    except Exception as err:
        print(err)
        await message.answer(
            "Couldn't solve the sudoku. Some error happened on the server-side or the image you sent is not sudoku! \nPlease, try again."
        )
