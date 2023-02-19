from .solve_board import solve_board


def get_board(board):
    """Takes the 9x9 grid matrix from unsolved sudoku board and returns a fully solved board"""
    if solve_board(board):
        # Return board if solved
        return board
    else:
        # Otherwise, raise ValueError
        raise ValueError