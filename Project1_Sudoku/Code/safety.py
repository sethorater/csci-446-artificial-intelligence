#--------------------------------------------------
# CHECK IF VALID MOVE AND CHECK IF EMPTY || PRINT FUNCTION TOO
#--------------------------------------------------

#------------------------------------------
# FUNCTIONS
#------------------------------------------

def checkIfSafe(puzzle, num, row, col):
    for x in range(9):
        if puzzle[row][x].number == num:
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

def checkEmpty(puzzle):
    for x in range(9):
        for y in range(9):
            if puzzle[x][y] == 0:
                return x, y
    return None

def printPuzzle(puzzle):
    for x in range(9):
        for y in range(9):
            print(puzzle[x][y].number, end=" ")
        print(" ")