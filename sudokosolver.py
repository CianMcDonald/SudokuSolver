import numpy as np

# board[x][y]
grid = [
    [5, 3, 4, 6, 7, 0, 0, 1, 2],
    [6, 0, 0, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 0, 4, 2, 0, 6, 7],
    [8, 5, 9, 0, 6, 0, 4, 2, 3],
    [4, 0, 0, 8, 0, 3, 7, 0, 1],
    [7, 0, 0, 0, 2, 0, 8, 5, 6],
    [9, 6, 0, 0, 0, 7, 2, 8, 0],
    [0, 9, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 5, 0, 8, 0, 1, 7, 9]
]
global board


def main():
    global board
    board = np.array(grid)
    print(board[0][4])


def selector(x, y, n):
    for num in range(9):
        # check if the n is on the row
        if board[x][num] == n:
            return False
        # check if the n is on the col
        if board[num][y] == n:
            return False
        # check square
    return True


if __name__ == "__main__":
    main()
