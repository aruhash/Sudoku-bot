import cv2, numpy as np


# Split the board into 81 individual images
def split_boxes(board, input_size: int = 48):
    """
    Takes the sudoku board and splits it into 81 cells.
    Each cell contains an element of the board, which is either given or an empty cell.
    """
    rows = np.vsplit(board, 9)
    boxes = []
    for r in rows:
        cols = np.hsplit(r, 9)
        for box in cols:
            box = cv2.resize(box, (input_size, input_size)) / 255.0
            boxes.append(box)
    cv2.destroyAllWindows()
    return boxes