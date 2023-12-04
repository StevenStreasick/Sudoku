import os
import Sudoku
import Backtracking
import GeneticAlgorithm
import xlwt
import time


numberOfBoards = 25

sudoku = Sudoku.Sudoku()

#Create an excel sheet to store the data
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Data")
#Fill out the table's headers.
header = xlwt.easyxf('font: bold 1, color red;')
sheet.write(0, 0, "Speed", header)
sheet.write(0, 1, "Backtracking", header)
sheet.write(0, 2, "Genetic Algorithm", header)

#Font characterization for the data values
speed = xlwt.easyxf('font: italic on, color black;')
#Just an incrememter to show progress. 
j = 0
#For all generated puzzles, iterate
for v in os.listdir("Puzzles"):
    #Incrementer
    j += 1
    print(j)

    #The current puzzle we are on. Numbered 1-24. 
    #I must've just forgotten to generate 25
    i = int(v.split(".")[0])

    #Load the puzzle
    sudoku.load("Puzzles/" + v)
    
    #Label the column with the puzzle value.
    sheet.write(i, 0, i)

    #Clock the amount of time it takes to solve via backtracking.
    beforeBacktracking = time.perf_counter()
    Backtracking.findSolution(sudoku.getBoard().getGrid()) 
    afterBacktracking = time.perf_counter()

    #Write the amount of time that it took to solve backtracking solution
    sheet.write(i, 1, afterBacktracking - beforeBacktracking, speed)

    #Clock the amount of time it takes to solve via GA.
    beforeGA = time.perf_counter()
    sol = GeneticAlgorithm.Solve(sudoku)   
    afterGA = time.perf_counter()
    
    #GA may generate a solution that is incomplete. We want to document this
    isValid = Sudoku.isValid(sol)
    
    if isValid:
        sheet.write(i, 2, afterGA - beforeGA, speed)
    else:
        sheet.write(i, 2, "-", speed)

#Create and save the excel sheet.
workbook.save("Calculations.xls")