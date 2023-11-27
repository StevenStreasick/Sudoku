import random
import Board
import Cell
import Backtracking

validValues = {1, 2, 3, 4, 5, 6, 7, 8, 9}


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
                if not grid[i][j].getCellValue() in validValues:
                    return False
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
def getUnfilledPositions(grid : list[list[type[Cell.Cell]]]) -> list[tuple[int]]:
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

    def __init__(self, difficulty : str = "Easy", size : tuple[int] = (9, 9)):
        #Contains a 'Has a' OOP structure instead of 'Is a'
        self._board = None
        #self._createGrid(difficulty, size)
        #self.

    #Uses a backtrack algorithm to determine if there exists a unique solution
    def _isUnique(self) -> bool:
        #Call upon a backtracking class to then implement a backtrack on the board.
        return Backtracking.isGridUnique(self._board.getGrid()) 
    
    def setBoard(self, board : type[Board.Board]):
        if not type(board) == type(Board.Board()):
            raise TypeError(board)
        if not isValid(board.getGrid()):
            raise ValueError(board)

        self._board = board
        
    
    def getBoard(self) -> type[Board.Board]:
        return self._board

    #Creates a full, or near full grid. 
    def createBoard(self, difficulty : str = "easy", size : tuple[int] = (9, 9)):
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
        board = None
        
        while not metDifficulty:
            board = Board.Board(size)
            grid = self._createFullGrid(size)
            board.setGrid(grid)
            self.setBoard(board)
            grid = self._trim()
            metDifficulty = True
            #TODO: Add a difficulty check.
        
            #if board.findDifficulty(board) = difficulty:
                #metDifficulty = True
        
        self.setBoard(board)
              
        return board

    #Returns the difficulty of a given board
    def findDifficulty(board : type[Board.Board]):
        grid = board.getGrid()
        emptyCell = 0
        for i in range(0, len(grid):
            emptyCell += grid[i].count("None")
        if emptyCell >= 54:
            return "hard"
        elif emptyCell >= 46:
            return "medium"
        else:
            return "easy"
            
    
    #BUG: Sometimes this function gets stuck and is unable to return a value.
    def _createFullGrid(self, size: tuple[int]):
       
        self.setBoard(Board.Board((9, 9)))
        grid = self.getBoard().getGrid()

        unvisitedPositions = getUnfilledPositions(grid)
        testIndex = 0
        while len(unvisitedPositions) > 0:
            print("i: " + str(testIndex))

            index = random.randint(0, len(unvisitedPositions) - 1)
            pos = unvisitedPositions[index]
            availableMoves = getValidCellValues(grid, pos)

            while len(availableMoves) > 0:
                i = random.randint(0, len(availableMoves) - 1)
                grid[pos[0]][pos[1]] = Cell.Cell(availableMoves[i])
                
                #As long as each number that we has still maintains at least one valid sol, then 
                #the end Grid will be a unique solution.
                
                if not Backtracking.findSolution(grid) == None:
                    #The added value still produces a solution, so I do not want to change this value.
                    break
                
                grid[pos[0]][pos[1]] = None
                availableMoves.pop(i)
                
            unvisitedPositions.pop(index)

            testIndex += 1
        #board.setBoard(grid)
        return grid


    #The goal of this method is to take a full, or near full, grid and to unfill in numbers such that a 
    #unique number still exists
    def _trim(self):
        
        grid = self.getBoard().getGrid()

        emptyBoard = Board.Board((len(grid), len(grid[0]))) 
        cellPos = getUnfilledPositions(emptyBoard.getGrid())
        flag = 0
        while len(cellPos) > 0:
            print(flag); flag += 1
            i = random.randint(0, len(cellPos) - 1)
            pos = cellPos.pop(i)
            cell = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = None
            
            if not self._isUnique():
                grid[pos[0]][pos[1]] = cell
        
        #self.getBoard().setGrid(grid)
        print(self.getBoard().getGrid())
        return grid
        

    def save(self, fileName : str):
        grid = self.getBoard().getGrid()

        with open(fileName, 'w') as f:


            for i in range(0, len(grid)):
                for j in range(0, len(grid[i])):
                    if not j == 0:
                        f.write(' ')

                    if grid[i][j] == None:
                        valToWrite = str(0)
                    else:
                        valToWrite = str(grid[i][j])
                    
                    f.write(valToWrite)
                f.write('\n')
        
    def load(self, fileName : str):
        board = Board.Board()
        grid = []
        #I need to construct a grid here from the text file.
        with open(fileName, 'r') as f:
            readRow = f.readline()
                        
            while not readRow == '':
                row = []

                for i in range(0, len(readRow)):
                    if readRow[i].isdigit():
                        num = int(readRow[i])
                        if num == 0:
                            row.append(None)
                        else:
                            row.append(Cell.Cell(int(readRow[i])))

                grid.append(row)
                readRow = f.readline()

        board.setGrid(grid) 
        self.setBoard(board)
