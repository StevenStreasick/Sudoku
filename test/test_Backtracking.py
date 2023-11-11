
import Backtracking
import Cell


def test_findsolution_randomBoard1():
    grid = [
            [
                None, Cell.Cell(1), None, 
                None, Cell.Cell(2), None,
                Cell.Cell(3), None, Cell.Cell(4)
            ],
            
            [
                None, None, Cell.Cell(5),
                None, None, Cell.Cell(3),
                Cell.Cell(6), None, None     
            ],
            [
                None, None, None, 
                Cell.Cell(7), None, None, 
                Cell.Cell(8), None, None
            ],
            
            [
                Cell.Cell(6), Cell.Cell(5), Cell.Cell(3), 
                None, None, Cell.Cell(7),
                None, None, Cell.Cell(8)
            ],
            [
                None, None, None,
                Cell.Cell(3), Cell.Cell(4), Cell.Cell(1),
                None, None, None
            ],
            [
                Cell.Cell(4), None, None,
                Cell.Cell(6), None, None,
                Cell.Cell(9), Cell.Cell(2), Cell.Cell(3)
            ],

            [
                None, None, Cell.Cell(2),
                None, None, Cell.Cell(6),
                None, None, None
            ],
            [  
                None, None, Cell.Cell(7), 
                Cell.Cell(8), None, None,
                Cell.Cell(2), None, None
            ],
            [
                Cell.Cell(3), None, Cell.Cell(9),
                None, Cell.Cell(7), None,
                None, Cell.Cell(5), None
            ]]
    
    foundSol = Backtracking.findSolution(grid)

    assert not foundSol == None, True
    
    sol = [[7, 1, 6, 5, 2, 8, 3, 9, 4], 
           [8, 9, 5, 4, 1, 3, 6, 7, 2], 
           [2, 3, 4, 7, 6, 9, 8, 1, 5], 
           [6, 5, 3, 2, 9, 7, 1, 4, 8], 
           [9, 2, 8, 3, 4, 1, 5, 6, 7], 
           [4, 7, 1, 6, 8, 5, 9, 2, 3], 
           [5, 4, 2, 9, 3, 6, 7, 8, 1], 
           [1, 6, 7, 8, 5, 4, 2, 3, 9], 
           [3, 8, 9, 1, 7, 2, 4, 5, 6]]
    for i in range(0, len(foundSol)):
        for j in range(0, len(foundSol[i])):
            assert foundSol[i][j].getCellValue() == sol[i][j], True

def test_findsolution_randomBoard2():
    grid = [
        [None, None, Cell.Cell(1),
         None, None, Cell.Cell(5),
         Cell.Cell(8), None, None],

        [Cell.Cell(2), Cell.Cell(8), None,
         None, None, Cell.Cell(3), 
         None, Cell.Cell(7), None],
         
        [None, None, Cell.Cell(4),
         Cell.Cell(2), None, None,
         None, None, None],


        [None, Cell.Cell(1), None, 
         None, None, None,
         None, None, None],
         
        [None, None, None, 
         None, Cell.Cell(5), None,
         None, Cell.Cell(4), None],

        [Cell.Cell(8), Cell.Cell(3), None,
         Cell.Cell(9), None, None, 
         Cell.Cell(5), None, None],
        

        [Cell.Cell(9), Cell.Cell(5), None,
         Cell.Cell(3), None, None, 
         Cell.Cell(4), None, None],

        [None, None, None, 
         None, None, Cell.Cell(7),
         None, None, Cell.Cell(6)],
        
        [None, None, Cell.Cell(2), 
         None, None, None,
         None, None, None]]
    
    foundSol = Backtracking.findSolution(grid)

    assert not foundSol == None
    
    sol = [[3, 9, 1, 6, 7, 5, 8, 2, 4], 
           [2, 8, 6, 4, 9, 3, 1, 7, 5], 
           [5, 7, 4, 2, 1, 8, 6, 3, 9], 
           [4, 1, 5, 7, 3, 6, 9, 8, 2], 
           [6, 2, 9, 8, 5, 1, 7, 4, 3], 
           [8, 3, 7, 9, 2, 4, 5, 6, 1], 
           [9, 5, 8, 3, 6, 2, 4, 1, 7], 
           [1, 4, 3, 5, 8, 7, 2, 9, 6], 
           [7, 6, 2, 1, 4, 9, 3, 5, 8]]
    
    for i in range(0, len(foundSol)):
        for j in range(0, len(foundSol[i])):
            assert foundSol[i][j].getCellValue() == sol[i][j], True


def test_isUnique_randomBoard1():
    grid = [
            [
                None, Cell.Cell(1), None, 
                None, Cell.Cell(2), None,
                Cell.Cell(3), None, Cell.Cell(4)
            ],
            
            [
                None, None, Cell.Cell(5),
                None, None, Cell.Cell(3),
                Cell.Cell(6), None, None     
            ],
            [
                None, None, None, 
                Cell.Cell(7), None, None, 
                Cell.Cell(8), None, None
            ],
            
            [
                Cell.Cell(6), Cell.Cell(5), Cell.Cell(3), 
                None, None, Cell.Cell(7),
                None, None, Cell.Cell(8)
            ],
            [
                None, None, None,
                Cell.Cell(3), Cell.Cell(4), Cell.Cell(1),
                None, None, None
            ],
            [
                Cell.Cell(4), None, None,
                Cell.Cell(6), None, None,
                Cell.Cell(9), Cell.Cell(2), Cell.Cell(3)
            ],

            [
                None, None, Cell.Cell(2),
                None, None, Cell.Cell(6),
                None, None, None
            ],
            [  
                None, None, Cell.Cell(7), 
                Cell.Cell(8), None, None,
                Cell.Cell(2), None, None
            ],
            [
                Cell.Cell(3), None, Cell.Cell(9),
                None, Cell.Cell(7), None,
                None, Cell.Cell(5), None
            ]]
     
    assert Backtracking.isGridUnique(grid) == True

def test_isUnique_randomBoard2():
    grid = [
        [None, None, Cell.Cell(1),
         None, None, Cell.Cell(5),
         Cell.Cell(8), None, None],

        [Cell.Cell(2), Cell.Cell(8), None,
         None, None, Cell.Cell(3), 
         None, Cell.Cell(7), None],
         
        [None, None, Cell.Cell(4),
         Cell.Cell(2), None, None,
         None, None, None],


        [None, Cell.Cell(1), None, 
         None, None, None,
         None, None, None],
         
        [None, None, None, 
         None, Cell.Cell(5), None,
         None, Cell.Cell(4), None],

        [Cell.Cell(8), Cell.Cell(3), None,
         Cell.Cell(9), None, None, 
         Cell.Cell(5), None, None],
        

        [Cell.Cell(9), Cell.Cell(5), None,
         Cell.Cell(3), None, None, 
         Cell.Cell(4), None, None],

        [None, None, None, 
         None, None, Cell.Cell(7),
         None, None, Cell.Cell(6)],
        
        [None, None, Cell.Cell(2), 
         None, None, None,
         None, None, None]]
    
    assert Backtracking.isGridUnique(grid) == False
