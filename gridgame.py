def gridgame(k, grid, rules):
    window = [[(i, j) for i in range(3)] for j in range(3)]
    row, col = len(grid), len(grid[0])
    neighbors = []
    adj = []
    print(grid)
    for turn in range(k):
        newgrid = []
        for i in range(row):
            newrow = []
            for j in range(col):
                x, y, alive = i - 1, j - 1, 0
                for m in range(3):
                    for n in range(3):
                        if x + m in range(row) and y + n in range(col):
                            if grid[x + m][y + n] == 1 and not (x+m == i and y+n == j):
                                alive += 1
                newrow.append(rules[alive])
            newgrid.append(newrow)
        print(newgrid)
        grid[:] = newgrid[:]

k = 2
grid = [[0, 1, 1, 0], [1, 1, 0, 0]]
rules = [0, 0, 0, 1, 0, 1, 0, 0, 0]
gridgame(k, grid, rules)