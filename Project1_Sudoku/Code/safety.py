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

    gridInQuestion = puzzle[row][col].grid
    for x in range(9):
        for y in range(9):
            if puzzle[x][y].grid == gridInQuestion and puzzle[x][y].number == num:
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

def getInitialDomain(puzzle):
    for x in range(9):
        for y in range(9):
            for i in range(1,10):
                if(checkIfSafe(puzzle, i, x, y)):
                    if (puzzle[x][y].number == 0):
                        puzzle[x][y].domain.append(i)
