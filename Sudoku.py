import random
import Board
import Cell
import Backtracking



@staticmethod
def isValid(grid : list[list[type[Cell.Cell]]]) -> bool:
    row = []; col = []; subgrid = []

    for i in range(0, len(grid)):
        row.append([])
        col.append([])
        subgrid.append([])

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if not grid[i][j] == None:
                if grid[i][j] in row[j]:
                    return False
                if grid[i][j] in col[i]:
                    return False
                if grid[i][j] in subgrid[j % 3 + (i % 3 * 3)]:
                    return False
                
                row[j].append(grid[i][j])
                col[i].append(grid[i][j])
                subgrid[j % 3 + (i % 3 * 3)].append(grid[i][j])
    return True


#I want Sudoku class to apply the constraints of Sudoku to the grid. 
@staticmethod
def getUnfilledPositions(grid : list[list[int]]) -> list[tuple[int]]:
    unfilledPositions = []

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == None:
                unfilledPositions.append((i, j))

    return unfilledPositions


#Returns the values that the specific cell can be.
@staticmethod
def getValidCellValues(grid : list[list[type[Cell.Cell]]], pos : tuple[int]) -> list[int]:

    #Must use a set to use intersection. Return as a list of ints.
    validValues = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    validRowValues = validValues.copy()
    validColValues = validValues.copy()
    validSubValues = validValues.copy()
    

    #Remove any invalid row values:
    for i in range(0, len(grid)):
        v = grid[i][pos[1]]
        if (not v == None) and v.getCellValue() in validRowValues:
            validRowValues.discard(v.getCellValue())

    #Remove any invalid column values
    for j in range(0, len(grid[pos[0]])):
        v = grid[pos[0]][j]

        if not v == None and v.getCellValue() in validColValues:             
            validColValues.discard(v.getCellValue())

    #Remove any invalid subgrid values
    for i in range(pos[0] - (pos[0] % 3), pos[0] - (pos[0] % 3) + 3):
        for j in range(pos[1] - (pos[1] % 3), pos[1] - (pos[1] % 3) + 3):
            v = grid[i][j]

            if not v == None and v.getCellValue() in validSubValues:
                validSubValues.remove(v.getCellValue())

    return list(validRowValues & validColValues & validSubValues)


class Sudoku:

    #TODO: Test all of these methods still
    def __init__(self, difficulty : str = "Easy", size : tuple[int] = (9, 9)):
        #Contains a 'Has a' OOP structure instead of 'Is a'
        self.board = None
        self._createGrid(difficulty, size)
        #self.

    #Uses a backtrack algorithm to determine if there exists a unique solution
    def _isUnique(self) -> bool:
        #Call upon a backtracking class to then implement a backtrack on the board.
        return Backtracking.isGridUnique(self.board.getGrid()) 


    #Creates a full, or near full grid. 
    def _createGrid(self, difficulty : str, size : tuple[int]):
        difficulties = ["easy", "medium", "hard"]

        if not type(difficulty) == str:
            raise TypeError(difficulty)
        
        difficulty = difficulty.lower()
        if not difficulty in difficulties:
            raise ValueError(difficulty)

        if not type(size) == tuple:
            raise TypeError(size)
        if not (type(size[0]) == int or type(size[1]) == int):
                raise TypeError(size)
        

        metDifficulty = False
        grid = None
        
        while not metDifficulty:
            self._createFullGrid(size)
            grid = self._trim()
            metDifficulty = True
            #TODO: Add a difficulty check.
              
        return grid
        
        
    def _createFullGrid(self, size: tuple[int]):
       
        self.board = Board.Board((9, 9))
        grid = self.board.getGrid()

        unvisitedPositions = getUnfilledPositions(grid)

        while len(unvisitedPositions) > 0:
            index = random.randint(0, len(unvisitedPositions) - 1)
            pos = unvisitedPositions[index]
            availableMoves = getValidCellValues(grid, pos)

            while len(availableMoves) > 0:
                grid[pos[0]][pos[1]] = Cell.Cell(availableMoves[random.randint(0, len(availableMoves) - 1)])
                
                if self._isUnique():
                    break

                grid[pos[0]][pos[1]] = None

            unvisitedPositions.pop(index)

        #board.setBoard(grid)
        return grid


    #The goal of this method is to take a full, or near full, grid and to unfill in numbers such that a 
    #unique number still exists
    def _trim(self):
        
        cellPos = []
        grid = self.board.getGrid()

        for i in range(0, 9):
            for j in range(0, 9):
                cellPos.append((i, j))
        
        random.shuffle(cellPos)

        while len(cellPos) > 0:
            i = random.randint(0, len(cellPos) - 1)
            pos = cellPos.pop(i)
            cell = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = None
            
            if not self._isUnique():
                grid[pos[0]][pos[1]] = cell

        return grid
        

    def save():
        pass
    def load():
        pass
    #TODO: Implement a save/load board method
