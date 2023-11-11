import random
import pytest
import Board
import Cell



def test_default_constructor():
    default_size = (9, 9)
    board = Board.Board().getGrid()
    if not len(board) == default_size[0]:
        raise Exception("The board was not set up properly")
    for i in range(0, len(board)):
        if not len(board[i]) == default_size[1]:
            raise Exception("The board was not set up properly")
        
def test_createEmptyBoard():
    boardClass = Board.Board()
    board = boardClass._createEmptyGrid((9, 9))

    if not len(board) == 9:
        raise Exception("The board was not set up properly")
    for i in range(0, len(board)):
        if not len(board[i]) == 9:
            raise Exception("The board was not set up properly")
        for j in range(0, len(board[i])):
            if not type(board[i][j]) == type(None):
                raise Exception("The createEmptyGrid function generated a non-empty board.")

def test_createRandomBoard():
    boardClass = Board.Board()

    board = boardClass._createRandomGrid((9, 9))
    if not len(board) == 9:
        raise Exception("The board was not set up properly")
    

    firstNum = None
    seenUnique = False

    for i in range(0, len(board)):
        if not len(board[i]) == 9:
            raise Exception("The board was not set up properly")
        for j in range(0, len(board[i])):
            if firstNum == None:
                firstNum = board[i][j]
            if not board[i][j] == firstNum:
                seenUnique = True

    assert seenUnique, True

def test_isFull_allones():
    board = []

    for i in range(0, 9):
        row = []

        for j in range(0, 9):
            cell = Cell.Cell(1)
            row.append(cell)

        board.append(row)

    boardClass = Board.Board((9,9))
    boardClass.setGrid(board)

    assert boardClass.isFull() == True

def test_isFull_varyingvalues():
    board = []

    for i in range(0, 9):
        row = []

        for j in range(0, 9):
            cell = Cell.Cell(random.randint(1, 9))
            row.append(cell)

        board.append(row)

    boardClass = Board.Board((9,9))
    boardClass.setGrid(board)

    assert boardClass.isFull() == True

def test_isFull_empty():
    boardClass = Board.Board((9,9))
    
    assert boardClass.isFull() == False

def test_isFull_partiallyEmpty():
    #Generate a partially empty board.
    board = []
    for i in range(0, 9):
        row = []
        for j in range(0, 9):
            if random.random() > .5:
                row.append(Cell.Cell(1))
        board.append(row)

    #Generate a boardClass
    boardClass = Board.Board((9, 9))
    #I cannot use the boardClass.setBoard() method, because it is designed to error. 
    boardClass.__grid = board 

    assert boardClass.isFull() == False



def test_setBoard_string():
    with pytest.raises(TypeError):
        board = Board()
        board.setGrid("Hello")
def test_setBoard_int():
    with pytest.raises(TypeError):
        board = Board()
        board.setGrid(5)
def test_setBoard_Cell():
    with pytest.raises(TypeError):
        cell = Cell.Cell()
        board = Board()
        board.setGrid(cell)
def test_setBoard_ListOfCells():
    with pytest.raises(TypeError):
        row = []
        for i in range(0, 9):
            row.append(Cell.Cell())
        board = Board()
        board.setGrid(row)
def test_setBoard_varyingsizes():
    with pytest.raises(TypeError):
        board = []

        for i in range(0, 9):
            row = []
        
            for j in range(0, random.randint(5, 9)):
                row.append(Cell.Cell(1))
        
            board.append(row)

        boardClass = Board((9, 9))
        boardClass.setGrid(board)
