import random

distances = [[0, 5, 2, 3, 7, 5, 6, 9],
             [5, 0, 3, 2, 3, 4, 7, 6],
             [2, 3, 0, 1, 2, 30, 7, 5],
             [3, 2, 1, 0, 12, 2, 3, 8],
             [7, 3, 2, 12, 0, 3, 2, 3],
             [5, 7, 30, 2, 3, 0, 1, 2],
             [6, 7, 4, 3, 2, 1, 0, 1],
             [9, 6, 5, 8, 3, 2, 1, 0]]


def generateRandomPopulation(populationSize):
    population = []
    while len(set(population)) < populationSize:
        numberOfWays = random.randint(0, 5)
        individual = '0'
        for i in range(numberOfWays):
            individual = individual + str(random.randint(1, 6))
        individual = individual + '7'
        population.append(individual)
    return set(population)



