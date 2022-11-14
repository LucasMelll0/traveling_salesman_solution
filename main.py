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
    # set() transforma a lista em um set, sets são listas que não possuem elementos repetidos
    # Enquanto o set population for menor que populationSize...
    while len(set(population)) < populationSize:
        # Quantidade aleatória de caminhos entre 0 e 7
        numberOfWays = random.randint(0, 5)
        # Individuo sempre começa no 0
        individual = '0'
        # Adiciona os caminhos aleatórios após o 0
        for i in range(numberOfWays):
            individual = individual + str(random.randint(1, 6))
        # Individuo sempre termina no 7
        individual = individual + '7'
        population.append(individual)

    return set(population)


def getFitness(population):
    fitness = {}
    for individual in population:
        cost = 0
        # For i para o tamanho do individuo
        for i in range(len(individual)):
            # Se não for o ultimo elemento
            if i < len(individual) - 1:
                # Pega a posição do eixo y na lista distances
                y = distances[int(individual[i])]
                # Pega a posição do eixo x na lista distances
                x = int(individual[i + 1])
                # Pega o valor na posição do eixo x
                value = y[x]
                # Adiciona ao custo
                cost = cost + value
        # Adiciona o individuo(key) com o custo(value) ao dict/map
        fitness[individual] = cost

    return fitness


def geneticAlgorithm(population):
    mutationProbability = 0.03
    newPopulation = []
    populationSize = len(population)
    while len(set(newPopulation)) < populationSize:
        individual1 = random.choice(list(population))
        individual2 = random.choice(list(population))
        offspring1 = individual1[0:len(individual1) - 1] + individual2[int((len(individual2) * 0.5)):]
        offspring2 = individual1[0:len(individual2) - 1] + individual2[int((len(individual1) * 0.5)):]

        #if random.random() < mutationProbability:


population = generateRandomPopulation(10)
fitness = getFitness(population)
print(list(population))
print(f"population: {population}")
individual1 = random.choice(list(population))
individual2 = random.choice(list(population))
print(f"individual 1: {individual1}, individual 2: {individual2}")
offspring1 = individual1[0:len(individual1) - 1] + individual2[int((len(individual2) * 0.5)):]
print(offspring1)
