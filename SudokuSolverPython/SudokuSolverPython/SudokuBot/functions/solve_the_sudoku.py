import cv2, numpy as np
from tensorflow.keras.models import load_model
from .find_board import find_board
from .split_boxes import split_boxes
from .get_board import get_board
from .display_numbers import display_numbers
from .get_InvPerspective import get_InvPerspective


def solve_the_sudoku(
    image: str, input_size: int = 48, model="DigitalRecognitionOCR.h5"
):
    """
    image - path to the image
    """
    classes = np.arange(0, 10)
    model = load_model(model)

    # Read the image
    img = cv2.imread(f"{image}")

    # Extract the board from an input image
    board, location = find_board(img)


    gray = cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)
    rois = split_boxes(gray)
    rois = np.array(rois).reshape(-1, input_size, input_size, 1)

    # Get prediction of model
    prediction = model.predict(rois)
    predicted_numbers = []

    # Get classes from prediction
    for i in prediction:
        # Returns the index of the maximum number of the array
        index = np.argmax(i)
        predicted_number = classes[index]
        predicted_numbers.append(predicted_number)

    # Reshape the list
    board_num = np.array(predicted_numbers).astype("uint8").reshape(9, 9)

    # Try to solve the board
    try:
        # Get the initial board
        solved_board_nums = get_board(board_num)

        # Create a binary array of the predicted numbers, where 0 represents unsolved block of sudoku, and 1 shows given number
        binArr = np.where(np.array(predicted_numbers) > 0, 0, 1)

        # Get only the solved numbers to fullfil the empty blocks of the board
        flat_solved_board_nums = solved_board_nums.flatten() * binArr

        # Create a mask
        mask = np.zeros_like(board)

        # Fill the empty positions with numbers
        solved_board_mask = display_numbers(mask, flat_solved_board_nums)
        inv = get_InvPerspective(img, solved_board_mask, location)
        combined = cv2.addWeighted(img, 0.7, inv, 1, 0)

        
        # Uncomment the code below if you want to represent the input image in a new window
        # cv2.imshow("Input image", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # Uncomment the code below if you want to show the result as an image in new window (without using telegram bot)
        # cv2.imshow("Solved version (by Aida)", combined)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        return combined
    except Exception as err:
        # "Debug" the exception
        print(f"ERROR: {err}")
        print("Solution couldn't be found. Model misread digits.")
