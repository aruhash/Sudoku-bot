
from .find_empty import find_empty
from .valid_board import valid_board


def solve_board(board):
    """Solves the sudoku"""
    # Find empty blocks
    is_empty = find_empty(board)

    # Is board empty?
    if not is_empty:
        # Yes, return True.
        return True
    else:
        # No, unpack and assign the tuple values to variables "row, col"
        row, col = is_empty

    for i in range(1, 10):
        if valid_board(board, i, (row, col)):
            board[row][col] = i

            if solve_board(board):
                # True, if solved
                return True

            # 0, if not solved
            board[row][col] = 0
    return False