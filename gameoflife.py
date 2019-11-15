def gameOfLife(board):
    rows = len(board)
    cols = len(board[0])
    newgrid = []
    for i in range(rows):
        newgridrow = []
        for j in range(cols):
            alive = 0
            for m in range(i - 1, i + 2):
                for n in range(j - 1, j + 2):
                    if m in range(rows) and n in range(cols) and not (m == i and n == j):
                        if board[m][n] == 1:
                            alive += 1
            if (alive < 2 or alive > 3) and board[i][j] == 1:
                newgridrow.append(0)
            elif alive == 3 and board[i][j] == 0:
                newgridrow.append(1)
            else:
                newgridrow.append(board[i][j])
        newgrid.append(newgridrow)
    return newgrid

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(gameOfLife(board))
