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
from fcAlgorithm import *

#------------------------------------------
# CREATE PUZZLE
#------------------------------------------

file = "../Puzzles/Hard-P1.txt"
puzzle = np.zeros((9, 9), dtype=object)
puzzle2 = np.zeros((9, 9), dtype=object)


importPuzzle(file, puzzle)
importPuzzle(file, puzzle2)

#------------------------------------------
# CALL ALGORITHM
#------------------------------------------

getInitialDomain(puzzle)

print("\nHere is the unsolved puzzle:\n")
printPuzzle(puzzle)
print("\nSolving...\n\nHere is the solved puzzle:\n")

fcAlg(puzzle, 0, 0)
printPuzzle(puzzle)

print("\nHere is the backtracking unsolved puzzle:\n")
printPuzzle(puzzle2)
print("\nSolving...\n\nHere is the solved puzzle:\n")

btAlg(puzzle2, 0, 0)
printPuzzle(puzzle2)