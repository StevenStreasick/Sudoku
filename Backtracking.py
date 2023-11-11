import Sudoku
import Cell

@staticmethod
def findSolution(gridOriginal : list[list[int]]):
    #TODO: Apply checks to the grid to confirm that it's a two dimensional array of ints.
    #Either returns none if no solution is found, or returns the solution found.
    grid = gridOriginal.copy()
    sol = _findSolutionHelper(grid)

    if sol == None:
        return None
    
    for i in range(0, len(sol)):
        for j in range(0, len(sol[i])):
            if sol[i][j] == None:
                return None
    return sol
    #Call findSolutionHelper(grid). Allows for this subgrid to be modified without directly copying a new grid each function call, which 
    #would be incredibly slow.
   



@staticmethod
def isGridUnique(gridOriginal : list[list[type[Cell.Cell]]]) -> bool:
    grid = gridOriginal.copy()
    return _isGridUniqueHelper(grid) == 1

def _isFull(grid : list[list[type[Cell.Cell]]]) -> bool:

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == None:
                return False
            
    return True

def _findSolutionHelper(grid):

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == None:
                possibleValues = Sudoku.getValidCellValues(grid, (i, j))
                
                for y in range(0, len(possibleValues)):
                    grid[i][j] = Cell.Cell(possibleValues[y])

                    filled = _findSolutionHelper(grid)

                    if not filled == None and _isFull(filled):
                        return filled
                    grid[i][j] = None
                return None
    #This is my base case. This assumes the puzzle is full. 
    return grid

def _isGridUniqueHelper(grid):
    hits = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == None:
                possibleValues = Sudoku.getValidCellValues(grid, (i, j))
                
                for y in range(0, len(possibleValues)):
                    grid[i][j] = Cell.Cell(possibleValues[y])

                    filled = _findSolutionHelper(grid)

                    if not filled == None and _isFull(filled):
                        hits += 1
                    grid[i][j] = None
                    if hits >= 2:
                        return hits
                
    #This is my base case. This assumes the puzzle is full. 
    return hits