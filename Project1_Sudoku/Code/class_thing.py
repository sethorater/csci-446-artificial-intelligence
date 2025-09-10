#--------------------------------------------------
# CLASS 'THING' AKA AN ELEMENT IN THE SUDOKU PUZZLE
#--------------------------------------------------

class Thing:
  def __init__(self, number, permanent, row, column, grid):
    self.number = number
    self.permanent = permanent
    self.row = row
    self.column = column
    self.grid = grid
