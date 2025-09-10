#------------------------------------------
# Name: Seth Keirn and Alex Knutson
# Date: 8_27_25
# Program: Sudoku Puzzle
# Class: CSCI 446
#------------------------------------------
# IMPORTS
#------------------------------------------

from puzzleImp import *
from btAlgorithm import *

#------------------------------------------
# CREATE PUZZLE
#------------------------------------------

file = "../Puzzles/Easy-P1.txt"
puzzle = np.zeros((9, 9), dtype=object)

importPuzzle(file, puzzle)

#------------------------------------------
# CALL ALGORITHM
#------------------------------------------

btAlg(puzzle)
