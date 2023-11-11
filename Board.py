import random
import Cell
class Board:
    def __init__(self, size : tuple[int] = (9, 9)):
        self.__grid = self._createEmptyGrid(size)
        pass

    #Determines if the grid is full. If any part of the grid has not been initialized, then it will 
    #return false.
    #Also returns false if any part of the grid has no size.
    def isFull(self):
        grid = self.__grid
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if not type(grid[i][j]) == Cell.Cell:
                    return False
            if len(grid[i]) == 0:
                return False
        if len(grid) == 0:
            return False
        return True
    
    def _createEmptyGrid(self, size : tuple[int]) -> list[list[type[Cell.Cell]]]:
        grid = []
        for i in range(0, size[0]):
            row = []

            for j in range(0, size[1]):
                row.append(None)

            grid.append(row)
        self.__grid = grid
        return grid

    def _createRandomGrid(self, size : tuple[int]) -> list[list[type[Cell.Cell]]]:
        grid = self._createEmptyGrid(size)
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                grid[i][j] = Cell.Cell(random.randrange(1, 9))

        return grid

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

    def getGrid(self) -> list[list[type[Cell.Cell]]]:
        return self.__grid