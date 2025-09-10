#------------------------------------------
# Name: Seth Keirn and Alex Knutson
# Date: 8_27_25
# Program: Sudoku Puzzle
# Class: CSCI 446
#------------------------------------------

# import numpy as np
# from class_thing import Thing
# from safety import checkIfSafe
from puzzleImp import *

# --------------------------------------------------
# IMPORT THE FILE || CREATE 2x2 ARRAY
# --------------------------------------------------

file = "../Puzzles/Easy-P1.txt"
puzzle = np.zeros((9, 9), dtype=object)

importPuzzle(file, puzzle)

# for i in range(9):
#     for j in range(9):
#         print(puzzle[i][j].number, end=" ")
#     print("")




