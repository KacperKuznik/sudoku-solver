board = [
    [0, 0, 3,  0, 2, 0,  6, 0, 0],
    [9, 0, 0,  3, 0, 5,  0, 0, 1],
    [0, 0, 1,  8, 0, 6,  4, 0, 0],

    [0, 0, 8,  1, 0, 2,  9, 0, 0],
    [7, 0, 0,  0, 0, 0,  0, 0, 8],
    [0, 0, 6,  7, 0, 8,  2, 0, 0],

    [0, 0, 2,  6, 0, 9,  5, 0, 0],
    [8, 0, 0,  2, 0, 3,  0, 0, 9],
    [0, 0, 5,  0, 1, 0,  3, 0, 0]]



def show():
    for row in board:
        print(*row)


def valid(x, y, n):
    if n in board[y] or n in list(zip(*board))[x]:
        return False

    col = x - x % 3
    row = y - y % 3

    for i in range(col, col+3):
        for j in range(row, row+3):
            if n == board[j][i]:
                return False
    return True


def find_empty_square():
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 0:
                return x,y
    return False


def solve():

    empty_square = find_empty_square()
    if empty_square:
        x, y = empty_square
    else:
        show()
        return True

    for n in range(1, 10):
        if valid(x, y, n):
            board[y][x] = n
            if solve():
                return True
            board[y][x] = 0
    return False


solve()
