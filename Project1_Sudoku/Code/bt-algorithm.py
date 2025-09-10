#------------------------------------------
# This is where the backtracking algorithm will be implemented
#------------------------------------------
from Project1_Sudoku.Code.main import puzzle
from safety import checkIfSafe
for x in range(9):
    print(" ")
    for y in range(9):
        print(puzzle[x][y].number, end=' ')
print(checkIfSafe(puzzle, 1, 0, 1))


