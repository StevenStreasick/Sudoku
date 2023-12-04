import copy
import Sudoku
import Cell


@staticmethod
# Returns the first solution found. If no solution is found, than None is returned.
def findSolution(gridOriginal : list[list[int]]):
    #TODO: Apply checks to the grid to confirm that it's a two dimensional array of ints.
    #Call findSolutionHelper(grid). Allows for this subgrid to be modified without directly copying a 
    # new grid each function call, which ould be incredibly slow.
    grid = copy.deepcopy(gridOriginal)
    sol = _findSolutionHelper(grid)

    if sol == None:
        return None
    #If the grid is not full. 
    #TODO: Call _isFull
    for i in range(0, len(sol)):
        for j in range(0, len(sol[i])):
            if sol[i][j] == None:
                return None
    return sol
    
   


#Determines if the grid is unique
@staticmethod
def isGridUnique(gridOriginal : list[list[type[Cell.Cell]]]) -> bool:
    #Find if more than one solution was found.
    grid = copy.deepcopy(gridOriginal)
    return _isGridUniqueHelper(grid) == 1

#Determines if the grid is full.
#Utilizes a never nesting philosophy
def _isFull(grid : list[list[type[Cell.Cell]]]) -> bool:

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == None:
                return False
            
    return True

#Finds a solution to the Sudoku puzzle. If one was not found, then it returns None. Works recursively.
#NOTE: function contains side effects. If you want to find a solution to a puzzle, use findSolution().
#This is for efficiency.
def _findSolutionHelper(grid):
    #Base case
    if _isFull(grid):
        return grid
    
    #Iterate over the grid
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            #If not value is found, then insert a value.
            if grid[i][j] == None:

                possibleValues = Sudoku.getValidCellValues(grid, (i, j))
                #Try each possible value in this spot.
                for y in range(0, len(possibleValues)):
    
                    grid[i][j] = Cell.Cell(possibleValues[y])

                    filled = _findSolutionHelper(grid)

                    if not filled == None and _isFull(filled):
                        return filled
                grid[i][j] = None
                #If no possible value for this index was found, then no solution exists.
                return None
    #Ideally, this is never reached.
    #BUG: I believe this should return the grid if it's reached down here, not None
    #This is because in order for it to enter here, it would have to never enter the if statement on line 58.
    return None

#Determines if one and only one solution to the Sudoku puzzle exists. Works recursively.
#NOTE: function contains side effects. If you want to find a solution to a puzzle, use findSolution().
#This is for efficiency.
def _isGridUniqueHelper(grid):
    #Base case
    if _isFull(grid):
        return 1
    
    #The number of solutions currently found
    hits = 0
    
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):

            if grid[i][j] == None:
                possibleValues = Sudoku.getValidCellValues(grid, (i, j))
                #No possible values for this grid. Means no possible solutions.
                if len(possibleValues) == 0:
                    return 0
                #Iterate over all possible values
                for y in range(0, len(possibleValues)):
                    #Try placing this value in this cell.
                    grid[i][j] = Cell.Cell(possibleValues[y])
                  
                    hits += _isGridUniqueHelper(grid)
                    #The below line has to come before we can return. Prevents an infinite cycle.    
                    #Restroes the value back to None.
                    grid[i][j] = None

                    #We can shortcircuit the number of hits if we know hits >= 2.
                    if hits >= 2:
                        return hits
                
                return hits
                
    #This is my base case. This assumes the puzzle is full. 
    return hits