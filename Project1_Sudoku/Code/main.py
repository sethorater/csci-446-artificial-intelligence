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
from safety import *

#------------------------------------------
# CREATE PUZZLE
#------------------------------------------

file = "../Puzzles/Insane-P1.txt"
puzzle = np.zeros((9, 9), dtype=object)

importPuzzle(file, puzzle)

#------------------------------------------
# CALL ALGORITHM
#------------------------------------------

print("\nHere is the unsolved puzzle:\n")
printPuzzle(puzzle)
print("\nSolving...\n\nHere is the solved puzzle:\n")

btAlg(puzzle, 0, 0)
printPuzzle(puzzle)

