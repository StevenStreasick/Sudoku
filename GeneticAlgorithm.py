import Sudoku
import Cell
import random
import copy

POPULATION_SIZE = 100
K_CHROMOSOMES = 7

def getValidGenes(grid, pos : tuple[int]):
    validGenes = []

    for i in range(1, len(grid)):
        validGenes.append(i)

    for i in range(pos[0] - (pos[0] % 3), pos[0] - (pos[0] % 3) + 3):
        for j in range(pos[1] - (pos[1] % 3), pos[1] - (pos[1] % 3) + 3):
            
            v = grid[i][j]

            if not v == None and v.getCellValue() in validGenes:
                validGenes.remove(v)

    return validGenes

#NOTE: I need to pass some reference to the grid.
def generateChromosome(grid):
    chromosome = copy.deepcopy(grid)

    for i in range(0, chromosome):
        for j in range(0, chromosome[i]):
            if not chromosome[i][j].isLocked():
                validGenes = getValidGenes(chromosome, (i, j))
                selectedGene = validGenes[random.randint(len(validGenes))]
                chromosome[i][j] = Cell.Cell(selectedGene)

    return chromosome


def fitness(grid):
    #Penalty score can be counted as the number of duplicates in each row/column
    penalty = 0
    foundColValues = []
    for i in range(0, len(grid)):
        foundRowValues = []

        for j in range(0, len(grid[i])):
            if i == 0:
                foundColValues.append([])
        
            foundVal = grid[i][j] #Might have to adjust this line based on what the grid is.
        
            if foundVal in foundRowValues:
                penalty += 1
            else:
                foundRowValues.append(foundVal)

            if foundVal in foundColValues[j]:
                penalty += 1
            else:
                foundColValues[j].append(foundVal)

    if penalty == 0:
        return 0
    #We want to try to reduce the penalty.
    return 1 / penalty
def getElite(p):
    #Loop through p, and check fitness(p). Return the table associated with the max of the values.
    pass

def crossover(chromosome1, chromosome2):
    child = []

    for blockIndex in range(0, len(chromosome1)):
        startPos = (blockIndex % 3, blockIndex // 3)
        coinFlip = random.randint(0, 1)
        chromosome = chromosome1 if coinFlip == 0 else chromosome1

        for i in range(startPos[0], startPos[0] - (startPos[0] % 3) + 3):
            for j in range(startPos[1], startPos[1] - (startPos[1] % 3) + 3):
                if j == 0:
                    child.append()
        #pos = (MAZECENTER - XOFFSET) if gameState.isRed(myPos) else (MAZECENTER + XOFFSET)



    #Select a parent block.
    return child

def kSelect(p):
    #Select fittest chromosome from a pool of k chromosomes. 
    #Select another fittest chromosome from a pool of k chromosomes (firstChromosome is excluded)
    #back into the population. This is repeated to select the second chromosome.
    popOne = []

    for _ in range(0, K_CHROMOSOMES):
        
        while True:
            i : int = random.randint(0, len(p))
            if p[i] in popOne:
                break

        popOne.append(p[i])

    firstChromosome = getElite(popOne)

    popTwo = []
    for _ in range(0, K_CHROMOSOMES):
        i : int = random.randint(0, len(p))
        #If i know the index, I can manipulate logic here a bit.

        while True:
            i : int = random.randint(0, len(p))
            if p[i] in popOne and not p[i] == firstChromosome:
                break
            
        popTwo.append(p[i])

    secondChromosome = getElite(popTwo)
    
    return firstChromosome, secondChromosome
#TODO: I need to mutate the child and the two parents. The better of the two parents will go on 
def mutate():
    #Swap two unlocked cells in the same block. 
    pass

def purge():
    #Crossover the whole population with the elite chromosome 
    #Mutate at least one genome per chromosome in population
    pass

#NOTE: I need to pass some reference to the grid.
def instantiatePopulation(grid, popSize : int):
    population = []

    for i in range(0, popSize):
        population.append(generateChromosome(grid))

    return population  

#Initialize Population P Done.
#Until stopping_criterion met:
# G = null
# while |G|≠ |P|
#   1. (C1, C2) = Select (P)
#   2. (Ch1, Ch2) = Crossover (C1, C2)
#   3. Ch1= Mutate (Ch1)
#   4. Ch2 = Mutate (Ch2)
#   5. Add Ch1 and Ch2 to G
# P = G 

@staticmethod
def Solution(sudoku : type[Sudoku.Sudoku]):
    
    p = instantiatePopulation(POPULATION_SIZE)
    #Loop while the fittest agent does not have a fitness of 0, or until max iterations is met.
        #iterate for # of children
            #I need to select from the population
            #I need to crossover my selection to produce two children. 
            #Mutate the children. 
            #Add 

        #If the new population has same fitness, increment flag.
        #Else, reset flag
        
        #If flag is over rho, then purge
