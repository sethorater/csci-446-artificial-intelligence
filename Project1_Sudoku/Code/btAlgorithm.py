#--------------------------------------------------
# BT (BACKTRACKING) ALGORITHM
#--------------------------------------------------

#------------------------------------------
# IMPORTS
#------------------------------------------

from safety import checkIfSafe

#------------------------------------------
# FUNCTIONS
#------------------------------------------

def btAlg(puzzle):
    for x in range(9):
        print(" ")
        for y in range(9):
            print(puzzle[x][y].number, end=' ')
    print(checkIfSafe(puzzle, 1, 0, 1))
