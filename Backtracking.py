import copy
import Sudoku
import Cell

#BUG: Sometimes gets stuck in an infinite loop.
#[[None, None, None, None, 5, None, None, None, None], 
#[None, None, 4, None, None, None, 1, None, 5], 
#[None, None, None, None, None, None, None, None, None], 
#[None, None, None, 5, None, None, None, None, 1], 
#[None, None, None, 2, 6, 9, None, 5, None], 
#[6, None, None, None, None, None, None, 9, None], 
#[None, None, None, None, 3, 1, None, None, None], 
#[None, None, None, None, None, None, 6, 7, None], 
#[None, None, None, None, None, None, None, None, None]]
@staticmethod
def findSolution(gridOriginal : list[list[int]]):
    #TODO: Apply checks to the grid to confirm that it's a two dimensional array of ints.
    #Either returns none if no solution is found, or returns the solution found.
    grid = copy.deepcopy(gridOriginal)
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
    grid = copy.deepcopy(gridOriginal)
    return _isGridUniqueHelper(grid) == 1

def _isFull(grid : list[list[type[Cell.Cell]]]) -> bool:

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == None:
                return False
            
    return True

#NOTE: function contains side effects. If you want to find a solution to a puzzle, use findSolution().
#This is for efficiency.
def _findSolutionHelper(grid):

    if _isFull(grid):
        return grid
    
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == None:

                possibleValues = Sudoku.getValidCellValues(grid, (i, j))
                
                for y in range(0, len(possibleValues)):
                    # print(str(i) + ' ' +  str(j) + ' ' + str(possibleValues[y]))
                    # print(grid)
    
                    grid[i][j] = Cell.Cell(possibleValues[y])

                    filled = _findSolutionHelper(grid)

                    if not filled == None and _isFull(filled):
                        return filled
                grid[i][j] = None
                
                return None
    #This is my base case. This assumes the puzzle has no solution. 
    
    return None

def _isGridUniqueHelper(grid):
    #Base case
    if _isFull(grid):
        return 1
    
    hits = 0
    
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == None:
                possibleValues = Sudoku.getValidCellValues(grid, (i, j))
                #No possible values for this grid. Means no possible solutions.
                if len(possibleValues) == 0:
                    return 0

                for y in range(0, len(possibleValues)):
                    grid[i][j] = Cell.Cell(possibleValues[y])
                  
                    hits += _isGridUniqueHelper(grid)
                    #The below line has to come before we can return. Prevents an infinite cycle.    
                    grid[i][j] = None

                    if hits >= 2:
                        return hits
                
                return hits
                
    #This is my base case. This assumes the puzzle is full. 
    return hits