import Sudoku
import Cell
import random
import copy

POPULATION_SIZE = 100
K_CHROMOSOMES = 7
MAX_ITERATIONS = 3000
MUTATION = .05
PARENTMUTATION = .5
IUNTILPERGE = 200

def getValidGenes(grid, pos : tuple[int]):
    validGenes = []

    for i in range(1, len(grid)):
        validGenes.append(i)

    for i in range(pos[0] - (pos[0] % 3), pos[0] - (pos[0] % 3) + 3):
        for j in range(pos[1] - (pos[1] % 3), pos[1] - (pos[1] % 3) + 3):
            
            v = grid[i][j]

            if not v == None and v.getCellValue() in validGenes:
                validGenes.remove(v.getCellValue())

    return validGenes

#NOTE: I need to pass some reference to the grid.
def generateChromosome(grid):
    chromosome = copy.deepcopy(grid)

    for i in range(0, len(chromosome)):
        for j in range(0, len(chromosome[i])):
            if not (chromosome[i][j] == None or chromosome[i][j].isLocked()):
                validGenes = getValidGenes(chromosome, (i, j))
                selectedGene = validGenes[random.randint(0, len(validGenes) - 1)]
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
    largestChromosome = None
    largestFitness = None

    for i in range(0, len(p)):
        chromosome = p[i]
        currentFitness = fitness(chromosome)

        if largestFitness == None or largestFitness < currentFitness:
            largestChromosome = chromosome
            largestFitness = currentFitness

    return largestChromosome

def crossover(chromosome1, chromosome2):
    child = []

    for i in range(0, len(chromosome1)):
        row = []
        for j in range(0, len(chromosome1[i])):
            row.append(None)
        child.append(row)

    for blockIndex in range(0, len(chromosome1)):
        startPos = (blockIndex // 3, blockIndex % 3)
        coinFlip = random.randint(0, 1)
        chromosome = chromosome1 if coinFlip == 0 else chromosome2

        for i in range(startPos[0], startPos[0] - (startPos[0] % 3) + 3):
            
            for j in range(startPos[1], startPos[1] - (startPos[1] % 3) + 3):
                child[i][j] = chromosome[i][j]

    #Select a parent block.
    return child

def kSelect(p):
    #Select fittest chromosome from a pool of k chromosomes. 
    #Select another fittest chromosome from a pool of k chromosomes (firstChromosome is excluded)
    #back into the population. This is repeated to select the second chromosome.
    popOne = []

    for _ in range(0, K_CHROMOSOMES):
        #I need to select a value
        #do until not p[i] in popOne
        while True:
            i : int = random.randint(0, len(p) - 1)
            if not p[i] in popOne:
                break

        popOne.append(p[i])

    firstChromosome = getElite(popOne)
    popTwo = []

    for _ in range(0, K_CHROMOSOMES):

        while True:
            i : int = random.randint(0, len(p) - 1)
            if not p[i] in popTwo and not p[i] == firstChromosome:
                break
            
        popTwo.append(p[i])

    secondChromosome = getElite(popTwo)
    
    return copy.deepcopy(firstChromosome), copy.deepcopy(secondChromosome)

def mutate(grid, mu):
    
    if mu < random.random():
        return grid
    #Swap two unlocked cells in the same block.
    blockIndex = random.randint(0, len(grid) - 1)

    genes = []
    for i in range(blockIndex // 3 * 3, blockIndex // 3 * 3 + 3):
        for j in range(blockIndex % 3 * 3, blockIndex % 3 * 3 + 3):

            genes.append((i, j))

    while len(genes) > 0:    
        
        pos1 = random.choice(genes)  
        gene1 = grid[pos1[0]][pos1[1]]

        if not gene1 == None and gene1.isLocked():
            genes.remove(pos1)
        break

    while len(genes) > 0:    
        
        pos2 = random.choice(genes)  
        gene2 = grid[pos2[0]][pos2[1]]

        if pos1 == pos2 or (not gene2 == None and gene2.isLocked()):
            genes.remove(pos2)
        
        break

    
    grid[pos1[0]][pos1[1]] = gene2
    grid[pos2[0]][pos2[1]] = gene1

    return grid            

def purge(p):
    #Crossover the whole population with the elite chromosome 
    #Mutate at least one genome per chromosome in population
    elite = getElite(p)
    newPop = []

    for i in range(0, len(p)):
        #TODO: Figure out how Purge() method works. 
        #Does it ignore the crossover between the elite and itself -> population size shrinks by 1
        #Does it randomly select another value to crossover?
        #Or does it just not care?
        #if not p[i] == elite:
        cv = crossover(p[i], elite)
        mutate(cv)
        newPop.append(cv)
        
    return newPop

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
def Solve(sudoku : type[Sudoku.Sudoku]):
    p = instantiatePopulation(sudoku.getBoard().getGrid(), POPULATION_SIZE)
    newP = []
    i = 0

    lastBest = None
    lastProdGen = 0;

    #I want the loop to exit when one of the conditions is false. When one condition false, return false
    while (not fitness(getElite(p)) == 0) and i < MAX_ITERATIONS:
        newP.append(getElite(p))

        while len(newP) < POPULATION_SIZE:
            (parent1, parent2) = kSelect(p)
            child = mutate(crossover(parent1, parent2), MUTATION)
            newP.append(child)
            #I only need to mutate if the probability is met
            newP.append(getElite([mutate(parent1, PARENTMUTATION), mutate(parent2, PARENTMUTATION)]))
        
        bestFitness = fitness(getElite(newP))
        print(bestFitness)

        if lastBest == bestFitness:
            lastProdGen += 1
        else:
            lastProdGen = 0

        lastBest = bestFitness

        if lastProdGen > IUNTILPERGE:
            purge(newP)

        p = newP
        newP = []
        

    return getElite(p)
    #Loop while the fittest agent does not have a fitness of 0, or until max iterations is met.
        #iterate for # of children
            #I need to select from the population
            #I need to crossover my selection to produce two children. 
            #Mutate the children. 
            #Add 

        #If the new population has same fitness, increment flag.
        #Else, reset flag
        
        #If flag is over rho, then purge
