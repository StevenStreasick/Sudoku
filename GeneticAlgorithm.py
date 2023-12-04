#This whole file was inspired by https://dl.acm.org/doi/abs/10.1145/3194452.3194463

import Sudoku
import Cell
import random
import copy

#The # of individuals per population
POPULATION_SIZE = 100
#The number of individuals to select for the K tournament
K_INDIVIDUALS = 7
#The max number of iterations before the algorithm gives us
MAX_ITERATIONS = 3000
#The rate at which children mutations occur.
MUTATION = .05
#The rate at which the parent causes mutations.
PARENTMUTATION = .5
#The number of iterations until a purge occurs
IUNTILPERGE = 200

#Returns all possible values based on the row/column constraints.
def getValidGenes(grid, pos : tuple[int]):
    validGenes = []

    for i in range(0, len(grid)):
        validGenes.append(i + 1)

    for i in range(pos[0] - (pos[0] % 3), pos[0] - (pos[0] % 3) + 3):
        for j in range(pos[1] - (pos[1] % 3), pos[1] - (pos[1] % 3) + 3):
            
            v = grid[i][j]

            if not v == None and v.getCellValue() in validGenes:
                validGenes.remove(v.getCellValue())

    return validGenes

#Takes a partially empty grid and fills it in
def generateChromosome(grid):
    #I want a unique reference to each chromosome. This will be iteratively called over same grid
    chromosome = copy.deepcopy(grid)

    for i in range(0, len(chromosome)):
        for j in range(0, len(chromosome[i])):
            #If I can modify the value, or no value exists
            if chromosome[i][j] == None or not chromosome[i][j].isLocked():
                #Randomly select a value
                validGenes = getValidGenes(chromosome, (i, j))
                selectedGene = validGenes[random.randint(0, len(validGenes) - 1)]
                chromosome[i][j] = Cell.Cell(selectedGene)

    return chromosome

#Determines how fit an individual is. Inversely porportional to the # of row/column violations
def fitness(grid):
    #Penalty score can be counted as the number of duplicates in each row/column
    penalty = 0
    foundColValues = []

    for i in range(0, len(grid)):
        foundRowValues = []

        for j in range(0, len(grid[i])):
            if i == 0:
                #If this is a new column, I need to append a column
                foundColValues.append([])
        
            
            if not grid[i][j] == None:
                foundVal = grid[i][j].getCellValue()
                #If the value was already in the row
                if foundVal in foundRowValues:
                    penalty += 1
                else:
                    #Note that we found this value in this row
                    foundRowValues.append(foundVal)
                #If the value was already in this column
                if foundVal in foundColValues[j]:
                    penalty += 1
                else:
                    #Note that we found this value in this column
                    foundColValues[j].append(foundVal)

    #NOTE: A divide by 0 bug will occur without this if statement. The returned val must be larger than
    #1  as 1/1 is 1
    if penalty == 0:
        return 2
    #We want to try to reduce the penalty. So return the inverse
    return 1 / penalty

#Returns the most fit individual for a population p
def getElite(p):
    #Loop through p, and check fitness(p). Return the value associated with the max of the values.
    #Keep track of the object with largest fitness
    largestChromosome = None
    #Keep track of the largest fitness
    largestFitness = None

    for i in range(0, len(p)):
        chromosome = p[i]
        currentFitness = fitness(chromosome)

        #Is there a new largest fitness?
        if largestFitness == None or largestFitness < currentFitness:
            largestChromosome = chromosome
            largestFitness = currentFitness

    return largestChromosome

#Breeds the two chromosomes, selecting random subgrids from each parent to make a child chromosome
def crossover(chromosome1, chromosome2):
    child = []

    #Fill out a blank child subgrid
    for i in range(0, len(chromosome1)):
        row = []
        for j in range(0, len(chromosome1[i])):
            row.append(None)
        child.append(row)

    #For every block, steal a chromosome from a parent
    for blockIndex in range(0, len(chromosome1)):
        #The first position of the subgrid
        startPos = (blockIndex // 3 * 3, blockIndex % 3 * 3)
        #Determines which parent to steal from
        coinFlip = random.randint(0, 1) 
        chromosome = chromosome1 if coinFlip == 0 else chromosome2

        #Steal this subgrid.
        for i in range(startPos[0], startPos[0] - (startPos[0] % 3) + 3):
            for j in range(startPos[1], startPos[1] - (startPos[1] % 3) + 3):
                child[i][j] = chromosome[i][j]

    return child

#Select two fittest individuals out of a random group.
#NOTE: Cannot generate two of the same individuals
def kSelect(p):
    #Select fittest chromosome from a pool of k chromosomes. 
    #Select another fittest chromosome from a pool of k chromosomes (firstChromosome is excluded)
    #back into the population. This is repeated to select the second chromosome.
    popOne = []

    for _ in range(0, K_INDIVIDUALS):
        #Initialize the subpopulation
        #do until not p[i] in popOne
        while True:
            #Randomly select an individual. If they are not already in the subpopulation, add them
            i : int = random.randint(0, len(p) - 1)
            if not p[i] in popOne:
                break

        #Add the individual to the subpopulation
        popOne.append(p[i])

    #Get the elite of the subpopulation
    firstChromosome = getElite(popOne)
    popTwo = []

    for _ in range(0, K_INDIVIDUALS):
        #Initialize the subpopulation
            #do until not p[i] in popOne and not elite individual previously found
        while True:
            #Randomly select an individual. If they are not already in the subpopulation, and are not 
            # previous elite, add them

            i : int = random.randint(0, len(p) - 1)
            if not p[i] in popTwo and not p[i] == firstChromosome:
                break

        #Add the individual to the subpopulation
        popTwo.append(p[i])

    #Get the elite of the subpopulation
    secondChromosome = getElite(popTwo)
    
    return copy.deepcopy(firstChromosome), copy.deepcopy(secondChromosome)

#Applies a mutation, swapping two genes in the same subgrid, every so often. 
# Rate of mutation scales with mu
def mutate(grid, mu):
    #If we make no changes, return
    if mu < random.random():
        return grid
    
    #Determine the block at which to swap two genes from.
    blockIndex = random.randint(0, len(grid) - 1)

    #Acts as all of the genes' positions within that subgrid
    genes = []
    for i in range(blockIndex // 3 * 3, blockIndex // 3 * 3 + 3):
        for j in range(blockIndex % 3 * 3, blockIndex % 3 * 3 + 3):

            genes.append((i, j))
    #While there are still values which we can select
    while len(genes) > 0:    
        
        pos1 = random.choice(genes)  
        gene1 = grid[pos1[0]][pos1[1]]
        #If we cannot modify this value, then remove it.
        #We chose to allow swaps with None, although, it really shouldn't make a difference as
        #pop gets their chromosomes fully filled in.
        if not gene1 == None and gene1.isLocked():
            genes.remove(pos1)
        break

    #Select a second gene to swap with   
    while len(genes) > 0:    
        
        pos2 = random.choice(genes)  
        gene2 = grid[pos2[0]][pos2[1]]
        #We do not want to be able to select the same value. 
        if pos1 == pos2 or (not gene2 == None and gene2.isLocked()):
            genes.remove(pos2)
        
        break

    #Swap the two genes
    grid[pos1[0]][pos1[1]] = gene2
    grid[pos2[0]][pos2[1]] = gene1

    return grid            

#Crossover the whole population with the elite chromosome 
#Mutate at least one genome per chromosome in population
def purge(p):
    
    elite = getElite(p)
    newPop = []

    for i in range(0, len(p)):
        #TODO: Figure out how Purge() method works. 
        #Does it ignore the crossover between the elite and itself -> population size shrinks by 1
        #Does it randomly select another value to crossover?
        #Or does it just not care?
        #if not p[i] == elite:
        cv = crossover(p[i], elite)
        mutate(cv, 1)
        newPop.append(cv)
        
    return newPop

#Creates a population full of randomly filled chromosomes.
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
#Utilizes a genetic algorithm to solve the Sudoku board. May not solve it completely
def Solve(sudoku : type[Sudoku.Sudoku]):
    #Create a population
    p = instantiatePopulation(sudoku.getBoard().getGrid(), POPULATION_SIZE)
    #Acts as the newest population. At the end of the iteration, it will become p
    newP = []
    #The current iteration
    i = 0

    #The last elite individual to have their fitness change
    lastBest = None
    #The length since the elite individual's fitness has changed
    lastProdGen = 0;
    best = fitness(getElite(p))

    #I want the loop to exit when one of the conditions is false. When one condition false, return false
    while (not best == 2) and i < MAX_ITERATIONS:
        #Pass forward the elite individual
        newP.append(getElite(p))

        #Continue creating new children for the population until our population size is reached
        while len(newP) < POPULATION_SIZE:
            #Select two parents
            (parent1, parent2) = kSelect(p)
            #Cross over/mutate the parents.
            child = mutate(crossover(parent1, parent2), MUTATION)
            #Add the child
            newP.append(child)
            #Mutate the two parents and then add the elite indivual.
            newP.append(getElite([mutate(parent1, PARENTMUTATION), mutate(parent2, PARENTMUTATION)]))
        
        elite = getElite(newP)
        best = fitness(elite)

        #Has the fitness of the elite changed?
        if lastBest == best:
            lastProdGen += 1
        else:
            lastProdGen = 0

        lastBest = best

        #Cause a purge if we're stuck in a local minima.
        if lastProdGen >= IUNTILPERGE:
            newP = purge(newP)

        p = newP
        newP = []
        i += 1
        

    return getElite(p)