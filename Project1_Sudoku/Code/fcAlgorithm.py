#--------------------------------------------------
# FC (FORWARD CHECKING) ALGORITHM
#--------------------------------------------------

#------------------------------------------
# IMPORTS
#------------------------------------------

from safety import *

#------------------------------------------
# FUNCTIONS
#------------------------------------------

def fcAlg(puzzle, row, col):

    if row == 8 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if puzzle[row][col].number != 0:
        return fcAlg(puzzle, row, col + 1)

    for num in puzzle[row][col].domain:
        if checkIfSafe(puzzle, num, row, col):
            puzzle[row][col].number = num
            if fcAlg(puzzle, row, col + 1):
                return True
            puzzle[row][col].number = 0

    return False