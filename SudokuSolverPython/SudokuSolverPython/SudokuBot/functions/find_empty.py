def find_empty(board):
    """Checks whether the block is empty or unsolved"""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # (row, col)
    return None
