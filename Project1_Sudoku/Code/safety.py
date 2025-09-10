def checkIfSafe(puzzle, num, row, col):
    for x in range(9):
        if puzzle[row][x] == num:
            return False

    for x in range(9):
        if puzzle[x][col].number == num:
            return False

    startrow = row - (row % 3)
    startcol = col - (col % 3)

    for i in range(3):
        for j in range(3):
            if puzzle[startrow + i][startcol + j].number == num:
                return False
    return True




