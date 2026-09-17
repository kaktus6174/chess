board = [["#" for _ in range(8)] for _ in range(8)]

def display_board():
    for row in board:
        row_string = ""
        for i in row:
            row_string += i
            row_string += " "
        print(row_string)