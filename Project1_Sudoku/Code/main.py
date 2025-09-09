# Name: Seth Keirn and Alex Knutson
# Date: 8_27_25
# Program: Sudoku Puzzle
# Class: CSCI 446
from ftplib import print_line

import numpy as np



print("This works!")

class Thing:
  def __init__(self, number, permanent, row, column, grid):
    self.number = number
    self.permanent = permanent
    self.row = row
    self.column = column
    self.grid = grid

#p1 = Thing(25, True, 26, 6)

#print(p1.number)
#print(p1.permanent)

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

for i in range(9):
    for j in range(9):
        print(i, j, puzzle[i][j].number)



