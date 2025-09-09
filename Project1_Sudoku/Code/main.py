# Name: Seth Keirn and Alex Knutson
# Date: 8_27_25
# Program: Sudoku Puzzle
# Class: CSCI 446

import numpy as np
from class_thing import Thing

# --------------------------------------------------
# IMPORT THE FILE || CREATE 2x2 ARRAY
# --------------------------------------------------

file = open("../Puzzles/Easy-P1.txt", encoding="utf-8-sig")

puzzle = np.zeros((9, 9), dtype=object)
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
        if num != 0:
            puzzle[rowSPot][colSpot] = Thing(num, True, rowSPot, colSpot, grid)
        else:
            puzzle[rowSPot][colSpot] = Thing(num, False, rowSPot, colSpot, grid)
        colSpot = colSpot + 1
    rowSPot += 1

# --------------------------------------------------



