import random
from tabulate import tabulate


def generate_board(size=10, mines=10):
    board = [["_" for _ in range(size+2)] for _ in range(size+2)]
    mines_location = []
    while mines > 0:
        x = random.randint(1, size)
        y = random.randint(1, size)
        loc = (x, y)
        if loc not in mines_location:
            mines_location.append(loc)
            mines -= 1
    for mine in mines_location:
        x, y = mine
        board[x][y] = "*"
    for i in range(1, size+1):
        for j in range(1, size+1):
            no_of_mines = 0
            if board[i][j] != "*":
                if board[i-1][j-1] == '*':
                    no_of_mines += 1
                if board[i-1][j] == '*':
                    no_of_mines += 1
                if board[i-1][j+1] == '*':
                    no_of_mines += 1
                if board[i][j-1] == '*':
                    no_of_mines += 1
                if board[i][j+1] == '*':
                    no_of_mines += 1
                if board[i+1][j-1] == '*':
                    no_of_mines += 1
                if board[i+1][j] == '*':
                    no_of_mines += 1
                if board[i+1][j+1] == '*':
                    no_of_mines += 1
                board[i][j] = no_of_mines
    del(board[0])
    del(board[-1])
    for i in board:
        i.pop(0)
        i.pop(-1)
    header = [i for i in range(size)]
    user_board = [['?' for i in range(size)] for j in range(size)]
    print(tabulate(board, tablefmt='pretty', headers=header, showindex=True))
    return (user_board, board)


def mining(user_board, board, row, col, dug):
    if board[row][col] == "*":
        return False
    elif board[row][col] > 0:
        dug.append((row, col))
        return dug
    dug.append((row, col))
    for r in range(max(0, row-1), min(len(board)-1, row+1)+1):
        for c in range(max(0, col-1), min(len(board)-1, col+1)+1):
            if ((r, c)) not in dug:
                dug.append((r, c))
                mining(user_board, board, r, c, dug)
    return dug


if __name__ == "__main__":
    dug = []
    user_board, board = generate_board(10, 10)
    print(tabulate(user_board, headers=[i for i in range(len(user_board))],
                   showindex=True, tablefmt="pretty"))
    while True:
        user_input = input(
            "input coorinates as row,col,'M'[optional] to mark as Mine:\n").split(",")
        if len(user_input) == 3:
            user_board[int(user_input[0])][int(user_input[1])] = "M"
        else:
            x, y = int(user_input[0]), int(user_input[1]),
            if (x, y) in dug:
                print("Already mined")
                continue
            a = mining(user_board, board, int(x), int(y), dug)
            if a == False:
                print("GAME OVER")
                print(tabulate(board, headers=[i for i in range(len(user_board))],
                               showindex=True, tablefmt="pretty"))
                break
            else:
                for val in dug:
                    x, y = val
                    user_board[x][y] = board[x][y]
                print(tabulate(user_board, headers=[i for i in range(len(user_board))],
                               showindex=True, tablefmt="pretty"))
