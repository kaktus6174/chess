board = [["#" for _ in range(8)] for _ in range(8)]
board[7][4] = "K"
for row in board:
    print(*row)
board[6][4], board[7][4] = board[7][4], board[6][4]
print()
for row in board:
    print(*row)