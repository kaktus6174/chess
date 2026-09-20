board = [["#" for _ in range(8)] for _ in range(8)]

def display_board():
    for row in board:
        row_string = ""
        for i in row:
            row_string += i
            row_string += " "
        print(row_string)

def set_starting_position():
    board[0][0], board[0][7] = "r", "r"
    board[0][1], board[0][6] = "n", "n"
    board[0][2], board[0][5] = "b", "b"
    board[0][3], board[0][4] = "q", "k"
    for i in range(8):
        board[1][i] = "p"

    board[7][0], board[7][7] = "R", "R"
    board[7][1], board[7][6] = "N", "N"
    board[7][2], board[7][5] = "B", "B"
    board[7][3], board[7][4] = "Q", "K"
    for i in range(8):
         board[6][i] = "P"
