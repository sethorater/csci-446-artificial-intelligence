# Name: Seth Keirn and Alex Knutson
# Date: 8_27_25
# Program: Sudoku Puzzle
# Class: CSCI 446
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

f = open("../Puzzles/Easy-P1.txt")

puzzle = np.zeros((9, 9), dtype=Thing)
print(puzzle)


