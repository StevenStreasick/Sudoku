import random
import Cell

#Holds a group of cells in a two dimensional grid. 
class Board:
    def __init__(self, size : tuple[int] = (9, 9)):
        self.__grid = self._createEmptyGrid(size)
        pass

    #Determines if the grid is full. If any part of the grid has not been initialized, then it will 
    #return false.
    #Utilizes a never nesting philosophy
    def isFull(self):
        grid = self.__grid

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                #If the value at grid[i][j] is not of Cell Type, then it is either null or 
                # improperly filled
                if not type(grid[i][j]) == Cell.Cell:
                    return False
            #The row has not been initialized.
            if len(grid[i]) == 0:
                return False
        #The grid has not been initialized.
        if len(grid) == 0:
            return False
        
        return True
    
    #Creates a grid with no values initialized and sets the current grid to this 'empty' grid.
    def _createEmptyGrid(self, size : tuple[int]) -> list[list[type[Cell.Cell]]]:
        grid = []

        for i in range(0, size[0]):
            row = []

            for j in range(0, size[1]):
                row.append(None)

            grid.append(row)
        self.__grid = grid
        return grid

    #Randomly selects a value between 1 and 9 for every slot.
    def _createRandomGrid(self, size : tuple[int]) -> list[list[type[Cell.Cell]]]:
        grid = self._createEmptyGrid(size)
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                grid[i][j] = Cell.Cell(random.randrange(1, 9))

        return grid
    
    #Sets the grid to the given value.
    #NOTE: the passed grid must be a square. 
    #Utilizes a never nesting philosophy
    def setGrid(self, grid):
        if not type(grid) == list:
            raise TypeError("setGrid takes in a list[list[int]]")
        if len(grid) == 0 or len(grid[0]) == 0:
            raise TypeError("setGrid requires an unempty list")

        rowLength = len(grid[0])

        for i in range(0, len(grid)):
            if not type(grid[i]) == list:
                raise TypeError("setGrid takes in a list[list[int]]")
            
            if not len(grid[i]) == rowLength:
                raise TypeError("setGrid requires the grid to be a rectangle")
    

        self.__grid = grid

    #Gets the current grid.
    def getGrid(self) -> list[list[type[Cell.Cell]]]:
        return self.__grid