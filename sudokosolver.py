import numpy as np

# board[x][y]
board = [
    [5, 3, 4, 6, 0, 0, 0, 1, 2],
    [6, 0, 0, 1, 9, 5, 3, 4, 8],
    [1, 9, 0, 0, 4, 2, 0, 6, 7],
    [8, 5, 0, 0, 6, 0, 4, 2, 3],
    [0, 0, 0, 8, 0, 3, 7, 0, 1],
    [0, 0, 0, 0, 2, 0, 8, 5, 6],
    [0, 6, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 5, 0, 0, 0, 1, 0, 0]
]


def solve():
    global board
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for n in range(1, 10):
                    if selector(row, col, n):
                        board[row][col] = n
                        solve()
                        board[row][col] = 0
                return
    print(np.array(board))
    input()


def selector(x, y, n):
    for num in range(9):
        # check if the n is on the row
        if board[x][num] == n:
            return False
        # check if the n is on the col
        if board[num][y] == n:
            return False
        # check square
    x = (x // 3) * 3
    y = (y // 3) * 3
    for row in range(x, x + 3):
        for col in range(y, y + 3):
            if board[row][col] == n:
                return False
    return True


solve()
