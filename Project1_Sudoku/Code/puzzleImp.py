# --------------------------------------------------
# IMPORT THE FILE || CREATE 2x2 ARRAY || RETURN PUZZLE
# --------------------------------------------------

#------------------------------------------
# IMPORTS
#------------------------------------------

import numpy as np
from class_thing import *

#------------------------------------------
# FUNCTIONS
#------------------------------------------

def importPuzzle(file, puzzle):
    file = open(file, encoding="utf-8-sig")

    counter = 0
    grid = 0
    rowSPot = 0

    for row in file:
        line = row.strip().split(",")
        colSpot = 0
        for val in line:
            if val == "?":
                num = 0
            else:
                num = int(val)

            if counter < 3:
                grid = 1
            elif counter < 6:
                grid = 2
            elif counter < 9:
                grid = 3
            elif counter < 12:
                grid = 1
            elif counter < 15:
                grid = 2
            elif counter < 18:
                grid = 3
            elif counter < 21:
                grid = 1
            elif counter < 24:
                grid = 2
            elif counter < 27:
                grid = 3
            elif counter < 30:
                grid = 4
            elif counter < 33:
                grid = 5
            elif counter < 36:
                grid = 6
            elif counter < 39:
                grid = 4
            elif counter < 42:
                grid = 5
            elif counter < 45:
                grid = 6
            elif counter < 48:
                grid = 4
            elif counter < 51:
                grid = 5
            elif counter < 54:
                grid = 6
            elif counter < 57:
                grid = 7
            elif counter < 60:
                grid = 8
            elif counter < 63:
                grid = 9
            elif counter < 66:
                grid = 7
            elif counter < 69:
                grid = 8
            elif counter < 72:
                grid = 9
            elif counter < 75:
                grid = 7
            elif counter < 78:
                grid = 8
            elif counter < 81:
                grid = 9
            if num != 0:
                puzzle[rowSPot][colSpot] = Thing(num, True, rowSPot, colSpot, grid)
            else:
                puzzle[rowSPot][colSpot] = Thing(num, False, rowSPot, colSpot, grid)
            colSpot = colSpot + 1
            counter = counter + 1
        rowSPot += 1
    return puzzle
