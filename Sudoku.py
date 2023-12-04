import random
import Board
import Cell
import Backtracking
import math

validValues = {1, 2, 3, 4, 5, 6, 7, 8, 9}


@staticmethod
#Determines whether a grid follows the constraints of Sudoku or not
def isValid(grid : list[list[type[Cell.Cell]]]) -> bool:
    row = []; col = []; subgrid = []

    for i in range(0, len(grid)):
        row.append([])
        col.append([])
        subgrid.append([])

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if not grid[i][j] == None:
                cellVal = grid[i][j].getCellValue()
                subgridIndex = (math.floor(j / 3)) + (math.floor(i / 3) * 3)
                if not cellVal in validValues:
                    return False
                if cellVal in row[i]:
                    return False
                if cellVal in col[j]:
                    return False
                if cellVal in subgrid[subgridIndex]:
                    return False
                
                row[i].append(cellVal)
                col[j].append(cellVal)
                subgrid[subgridIndex].append(cellVal)
    return True


#Returns a list of positions that have no value associated with them within the grid.
@staticmethod
def getUnfilledPositions(grid : list[list[type[Cell.Cell]]]) -> list[tuple[int]]:
    unfilledPositions = []

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == None:
                unfilledPositions.append((i, j))

    return unfilledPositions


#Returns the values that the specific cell can be based on the constraints of Sudoku.
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

    #Return the intersection of the valid values.
    return list(validRowValues & validColValues & validSubValues)

#Creates a new, locked cell. 
def createCell(val : int) -> type[Cell.Cell]:
        cell = Cell.Cell(val)
        cell.lock()

        return cell

#Applies the constraints of Sudoku to the board class
class Sudoku:
    #Creates a new Sudoku class. 
    #NOTE: The user must still set up the board for the Sudoku class. This can be done by calling
    #setBoard, createEmptyBoard, or createBoard
    def __init__(self, difficulty : str = "Easy", size : tuple[int] = (9, 9)):
        #Contains a 'Has a' OOP structure instead of 'Is a'
        self._board = None
        #self._createGrid(difficulty, size)
        #self.

    #Uses a backtrack algorithm to determine if there exists a unique solution
    def _isUnique(self) -> bool:
        return Backtracking.isGridUnique(self._board.getGrid()) 
    
    #Sets the board variable to the passed board. 
    #NOTE: board must be a valid sudoku board. 
    def setBoard(self, board : type[Board.Board]):
        if not type(board) == type(Board.Board()):
            raise TypeError(board)
        if not isValid(board.getGrid()):
            raise ValueError(board)

        self._board = board
        
    #Returns the current board
    def getBoard(self) -> type[Board.Board]:
        return self._board
    
    #Sets the current board to an empty board.
    def createEmptyBoard(self, size : tuple[int] = (9, 9)):
        
        self.setBoard(Board.Board(size))



    #Creates a full grid. 
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
        isPuzzleValid = False
        
        #NOTE: Because of time constraints with generating puzzles, we chose to exlude difficulty
        #Continue to create puzzles until a puzzle with that difficulty is made. 
        while not metDifficulty and not isPuzzleValid:
            board = Board.Board(size)
            #Best to ensure that a valid grid is actually created. 
            grid = self._createFullGrid(size)

            
            if Sudoku.isValid(grid):
                isPuzzleValid = True
                board.setGrid(grid)
                self.setBoard(board)

                grid = self._trim()
                metDifficulty = True

                #if board.findDifficulty(board) = difficulty:
                    #metDifficulty = True

        self.setBoard(board)
              
        return board
    
    
        
    #Returns the difficulty of a given board
    #NOTE: There are many, many factors that go into difficulty, and this is a very rudimentary 
    #      difficulty checker
    def findDifficulty(self):
        grid = self.getBoard().getGrid()
        emptyCell = 0
        
        #For each row, sum the number of occurances of 'None'
        for i in range(0, len(grid)):
            emptyCell += grid[i].count("None")

        if emptyCell >= 54:
            return "hard"
        elif emptyCell >= 46:
            return "medium"
        else:
            return "easy"

    #Generates a full grid.
    #NOTE: I have found evidence to suggest that a bug may exist in the performance of creating grids
    #      but I have no reason to suspect this affected test results 
    #Took inspiration from https://stackoverflow.com/questions/6924216/how-to-generate-sudoku-boards-with-unique-solutions
    def _createFullGrid(self, size: tuple[int]):
       
        self.createEmptyBoard(size)
        grid = self.getBoard().getGrid()

        unvisitedPositions = getUnfilledPositions(grid)
        #While we can still try positions. 
        while len(unvisitedPositions) > 0:
            #Select a random position
            index = random.randint(0, len(unvisitedPositions) - 1)
            pos = unvisitedPositions[index]
            
            availableMoves = getValidCellValues(grid, pos)

            #Try all available values for this random position
            while len(availableMoves) > 0:
                i = random.randint(0, len(availableMoves) - 1)
                grid[pos[0]][pos[1]] = createCell(availableMoves[i])
                
                #As long as each number that we has still maintains at least one valid sol, then 
                #the end Grid will be a unique solution.
                
                if not Backtracking.findSolution(grid) == None:
                    #The added value still produces a solution, so I do not want to change this value.
                    break
                
                #The grid no longer produces a solution -> we have to backtrack.
                grid[pos[0]][pos[1]] = None
                availableMoves.pop(i)
                
            unvisitedPositions.pop(index)
        #NOTE: Automatically adjusts the pointers, so setting the board to this grid is redundant
        #board.setBoard(grid)
        return grid


    #The goal of this method is to take a full, or near full, grid and to unfill in numbers such that a 
    #unique solution still exists
    #Inspired by https://stackoverflow.com/questions/6924216/how-to-generate-sudoku-boards-with-unique-solutions
    def _trim(self):
        
        grid = self.getBoard().getGrid()

        emptyBoard = Board.Board((len(grid), len(grid[0]))) 
        cellPos = getUnfilledPositions(emptyBoard.getGrid())


        #While we have not tried removing all values
        while len(cellPos) > 0:
            #The index that we want to remove a value from.
            i = random.randint(0, len(cellPos) - 1)
            #The position in grid of the value we want to try to remove
            pos = cellPos.pop(i)

            cell = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = None
            
            #If removing the value results in a non unique grid, then we want to readd it
            if not self._isUnique():
                grid[pos[0]][pos[1]] = cell
        
        #self.getBoard().setGrid(grid)
        return grid
        
    #Saves the grid to a file. 
    #BUG: Does not save locked/unlocked values. Locked/Unlocked values were added after save/load.
    def save(self, fileName : str):
        grid = self.getBoard().getGrid()

        #Opens and closes the file when finished
        with open(fileName, 'w') as f:
        
            for i in range(0, len(grid)):
                for j in range(0, len(grid[i])):
                    #We want to add a space inbetween values to make the saved grid 'pretty'
                    if not j == 0:
                        f.write(' ')

                    #Replace 'None' with 0 in order to write a one digit number to the save. 
                    #Makes loading much easier
                    if grid[i][j] == None:
                        valToWrite = str(0)
                    else:
                        valToWrite = str(grid[i][j])
                    
                    f.write(valToWrite)
                f.write('\n')
    #Loads the current grid with the saved grid
    #BUG: Automatically assumes all cells were locked. 
    def load(self, fileName : str):
        board = Board.Board()
        grid = []

        #Opens and closes the file when finished
        with open(fileName, 'r') as f:
            readRow = f.readline()
            #Iterate over the row, adding all values into an array, which will act as the row. 
            while not readRow == '':
                row = []

                for i in range(0, len(readRow)):
                    if readRow[i].isdigit():
                        #Read the number
                        num = int(readRow[i])
                        #0 represents a None value.
                        if num == 0:
                            row.append(None)
                        else:
                            row.append(createCell(int(readRow[i])))

                grid.append(row)
                readRow = f.readline()

        board.setGrid(grid) 
        self.setBoard(board)
