import random

import pytest
import Sudoku
import Cell

def test_defaultconstructor():
    #TODO: Add an implementation to determine the difficulty of the puzzle
    
    default_size = (9, 9)
    board = Sudoku.Sudoku().board
    grid = board.getGrid()
    #if not type(sud) == list[li]
    if not len(grid) == default_size[0]:
        raise Exception("The Sudoku board was not set up properly")
    for i in range(0, len(grid)):
        if not len(grid[i]) == default_size[1]:
            raise Exception("The Sudoku board was not set up properly")
        
    assert False, board.isFull()


def test_isUnique():
    pass


def test_getUnfilledPositions_empty():
    grid = []

    for i in range(0, 9):
        row = []
        for j in range(0, 9):
            row.append(None)
        grid.append(row)

    getUnfilledPos = Sudoku.getUnfilledPositions(grid)

    assert len(getUnfilledPos), 81
    
    for i in range(0, 9):
        for j in range(0, 9):
            assert (i, j) in getUnfilledPos, True

def test_getUnfilledPositions_emptybuttopcorner():
    grid = []

    for i in range(0, 9):
        row = []
        for j in range(0, 9):
            row.append(None)
        grid.append(row)

    grid[0][0] = Cell.Cell(5)


    getUnfilledPos = Sudoku.getUnfilledPositions(grid)

    assert len(getUnfilledPos), 80
    
    for i in range(0, 9):
        for j in range(0, 9):
            if not (i == 0 and j == 0):
                assert (i, j) in getUnfilledPos, True

def test_getUnfilledPositions_emptybutbottomcorner():
    grid = []

    for i in range(0, 9):
        row = []
        for j in range(0, 9):
            row.append(None)
        grid.append(row)

    grid[8][8] = Cell.Cell(5)

   

    getUnfilledPos = Sudoku.getUnfilledPositions(grid)

    assert len(getUnfilledPos), 80
    
    for i in range(0, 9):
        for j in range(0, 9):
            if not (i == 8 and j == 8):
                assert (i, j) in getUnfilledPos, True

def test_getUnfilledPositions_full():
    grid = []

    for i in range(0, 9):
        row = []
        for j in range(0, 9):
            row.append(Cell.Cell(random.randint(1, 9)))
        grid.append(row)

    unfilledPos = Sudoku.getUnfilledPositions(grid)

    assert len(unfilledPos) == 0, True


def test_getUnfilledPositions_fullbutbottomcorner():
    grid = []

    for i in range(0, 9):
        row = []
        for j in range(0, 9):
            row.append(Cell.Cell(random.randint(1, 9)))
        grid.append(row)

    grid[8][8] = None

    unfilledPos = Sudoku.getUnfilledPositions(grid)

    assert len(unfilledPos) == 1, True
    assert (8, 8) in unfilledPos, True

def test_getUnfilledPositions_partial1():

    grid = [
        [Cell.Cell(3), None, Cell.Cell(9), None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None], 
        [None, Cell.Cell(4), None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, Cell.Cell(3), None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Cell.Cell(6), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Cell.Cell(9), None, None, Cell.Cell(2), None, None, None],
        [None, None, None, None, None, None, None, None, Cell.Cell(1)]
    ] #Eight filled in values at (0, 0), (0, 2), (2, 1), (3, 8), (5, 3), (7, 2), (7, 5), (8, 8)
    vals = [(0, 0), (0, 2), (2, 1), (3, 7), (5, 3), (7, 2), (7, 5), (8, 8)]

    unfilledPos = Sudoku.getUnfilledPositions(grid)
    assert len(unfilledPos) == 81 - len(vals), True

    for i in range(0, len(vals)):
        if vals[i] in unfilledPos:
            raise Exception("The getUnfilledPositions method should not return filled positions.")

def test_getUnfilledPositions_partial2():

    grid = [
        [None, None, None, None, None, None, Cell.Cell(7), None, None],
        [None, None, None, None, None, None, None, Cell.Cell(8), None], 
        [None, None, None, None, None, None, None, None, Cell.Cell(9)],
        [Cell.Cell(1), None, None, None, None, None, None, None, None],
        [None, Cell.Cell(2), None, None, None, None, None, None, None],
        [None, None, Cell.Cell(3), None, None, None, None, None, None],
        [None, None, None, Cell.Cell(4), None, None, None, None, None],
        [None, None, None, None, Cell.Cell(5), None, None, None, None],
        [None, None, None, None, None, Cell.Cell(6), None, None, None]
    ] #Eight filled in values at (0, 6), (1, 7), (2, 8), (3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)
    vals = [(0, 6), (1, 7), (2, 8), (3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)]

    unfilledPos = Sudoku.getUnfilledPositions(grid)
    assert len(unfilledPos) == 81 - len(vals), True

    for i in range(0, len(vals)):
        if vals[i] in unfilledPos:
            raise Exception("The getUnfilledPositions method should not return filled positions.")

def test_getUnfilledPositions_partial3():
    grid = [
        [Cell.Cell(1), Cell.Cell(2), None, None, None, None, None, Cell.Cell(5), Cell.Cell(6)],
        [Cell.Cell(3), Cell.Cell(4), None, None, None, None, None, Cell.Cell(7), Cell.Cell(8)], 
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [Cell.Cell(1), Cell.Cell(2), None, None, None, None, None, Cell.Cell(5), Cell.Cell(6)],
        [Cell.Cell(3), Cell.Cell(4), None, None, None, None, None, Cell.Cell(7), Cell.Cell(8)]
    ] #Eight filled in values at (0, 6), (1, 7), (2, 8), (3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)
    vals = [(0, 0), (0, 1), (0, 7), (0, 8), (1, 0), (1, 1), (1, 7), (1, 8), (7, 0), (7, 1), (7, 7), (7, 8), (8, 0), (8, 1), (8, 7), (8, 8)]

    unfilledPos = Sudoku.getUnfilledPositions(grid)
    assert len(unfilledPos) == 81 - len(vals), True

    for i in range(0, len(vals)):
        if vals[i] in unfilledPos:
            raise Exception("The getUnfilledPositions method should not return filled positions.")
        
def test_getValidCellValues_novalidoptions():

    grid = [
        [Cell.Cell(1), Cell.Cell(2), None, None, None, None, None, Cell.Cell(5), Cell.Cell(6)],
        [None, None, None, Cell.Cell(9), Cell.Cell(3), Cell.Cell(8), None, None, None], 
        [None, None, None, None, Cell.Cell(4), None, None, None, None],
        [None, None, None, None, Cell.Cell(7), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None]
    ] #Eight filled in values at (0, 6), (1, 7), (2, 8), (3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)


    validCells = Sudoku.getValidCellValues(grid, (0, 4))
    assert len(validCells) == 0, True
    assert validCells == [], True

def test_getValidCellValues_emptygrid():

    grid = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None], 
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None]
    ] 


    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            validCells = Sudoku.getValidCellValues(grid, (i, j))
            assert len(validCells) == 9, True
            assert validCells == [1, 2, 3, 4, 5, 6, 7, 8, 9], True

def test_getValidCellValues_allvalidcells():

    grid = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Cell.Cell(9), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5)], 
        [None, None, None, Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6)],
        [None, Cell.Cell(9), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7)],
        [None, Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8)],
        [None, Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9)],
        [None, Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9), Cell.Cell(1)],
        [None, Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9), Cell.Cell(1), Cell.Cell(2)],
        [None, Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3)]
    ] 



    validCells = Sudoku.getValidCellValues(grid, (0, 0))
    assert len(validCells) == 9, True
    assert validCells == [1, 2, 3, 4, 5, 6, 7, 8, 9], True


def test_getValidCellValues_somevalidcells1():
    grid = [
        [None, Cell.Cell(2), None, None, None, None, None, None, None],
        [None, None, None, Cell.Cell(9), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5)], 
        [None, None, Cell.Cell(4), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6)],
        [None, Cell.Cell(9), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7)],
        [None, Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8)],
        [None, Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9)],
        [None, Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9), Cell.Cell(1)],
        [None, Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9), Cell.Cell(1), Cell.Cell(2)],
        [Cell.Cell(7), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3)]
    ] 

    actualValidCells = [1, 3, 5, 6, 8, 9]


    validCells = Sudoku.getValidCellValues(grid, (0, 0))
    assert len(validCells) == len(actualValidCells), True
    assert validCells == actualValidCells, True

def test_getValidCellValues_somevalidcells2():

    grid = [
        [None, Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), None, None, None, None, None],
        [None, Cell.Cell(1), None, Cell.Cell(9), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5)], 
        [None, None, Cell.Cell(4), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6)],
        [Cell.Cell(7), Cell.Cell(9), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7)],
        [None, Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8)],
        [None, Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9)],
        [None, Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9), Cell.Cell(1)],
        [None, Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9), Cell.Cell(1), Cell.Cell(2)],
        [Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3)]
    ] 

    actualValidCells = [5, 6, 8, 9]

    validCells = Sudoku.getValidCellValues(grid, (0, 0))
    validCells.sort()
    assert len(validCells) == len(actualValidCells), True
    assert validCells == actualValidCells, True

def test_getValidCellValues_avalidcell():
    grid = [
        [None, Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(6), Cell.Cell(7), None, None, None],
        [None, Cell.Cell(1), Cell.Cell(8), Cell.Cell(9), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5)], 
        [None, Cell.Cell(9), Cell.Cell(4), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6)],
        [Cell.Cell(7), Cell.Cell(9), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7)],
        [None, Cell.Cell(1), Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8)],
        [None, Cell.Cell(2), Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9)],
        [None, Cell.Cell(3), Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9), Cell.Cell(1)],
        [None, Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9), Cell.Cell(1), Cell.Cell(2)],
        [Cell.Cell(4), Cell.Cell(5), Cell.Cell(6), Cell.Cell(7), Cell.Cell(8), Cell.Cell(9), Cell.Cell(1), Cell.Cell(2), Cell.Cell(3)]
    ] 

    actualValidCells = [5]


    validCells = Sudoku.getValidCellValues(grid, (0, 0))
    validCells.sort()
    assert len(validCells) == len(actualValidCells), True
    assert validCells == actualValidCells, True

def test_createGrid_invaliddifficultyvalue():
    with pytest.raises(ValueError):
        sud = Sudoku.Sudoku()._createGrid("Difficult", (9, 9))
    with pytest.raises(ValueError):
        sud = Sudoku.Sudoku()._createGrid("Mediocre", (9, 9))

def test_createGrid_invaliddifficultytype():
    with pytest.raises(TypeError):
        sud = Sudoku.Sudoku()._createGrid(1, (9, 9))
    with pytest.raises(TypeError):
        sud = Sudoku.Sudoku()._createGrid([1], (9, 9))

def test_createGrid_invalidsizetype():
    with pytest.raises(TypeError):
        sud = Sudoku.Sudoku()._createGrid("Easy", 5)   
    with pytest.raises(TypeError):
        sud = Sudoku.Sudoku()._createGrid("Medium", ("Hello ", "World"))
#TODO: Create createGrid tests to test the difficulty of the board. 
def test_createGrid_easy():
    sud = Sudoku.Sudoku()
    easyBoard = sud._createGrid("Easy", (9, 9))
    isFilled = True

    for i in range(0, len(easyBoard)):
        for j in range(0, len(easyBoard[i])):
            if easyBoard[i][j] == None:
                isFilled = False

    assert isFilled, False
    assert sud._isUnique(easyBoard), True
    assert len(easyBoard) == 9, True
    assert len(easyBoard[0]) == 9, True

def test_createGrid_medium():
    sud = Sudoku.Sudoku()
    easyBoard = sud._createGrid("Medium", (9, 9))
    isFilled = True

    for i in range(0, len(easyBoard)):
        for j in range(0, len(easyBoard[i])):
            if easyBoard[i][j] == None:
                isFilled = False

    assert isFilled, False
    assert sud._isUnique(easyBoard), True
    assert len(easyBoard) == 9, True
    assert len(easyBoard[0]) == 9, True

def test_createGrid_hard():
    sud = Sudoku.Sudoku()
    easyBoard = sud._createGrid("hard", (9, 9))
    isFilled = True

    for i in range(0, len(easyBoard)):
        for j in range(0, len(easyBoard[i])):
            if easyBoard[i][j] == None:
                isFilled = False

    assert isFilled, False
    assert sud._isUnique(easyBoard), True
    assert len(easyBoard) == 9, True
    assert len(easyBoard[0]) == 9, True

def test_isValid_oneitem():

    grid = [
        [Cell.Cell(1), None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None], 
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None]
    ] 


    assert Sudoku.isValid(grid), True
#TODO: Test isValid more

#TODO: Test isUnique
#TODO: Test save/load board