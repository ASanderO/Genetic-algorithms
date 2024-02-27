import random

names = ['Saco de dormir', 'Corda', 'Canivete', 'Tocha', 'Garrafa', 'Comida']
weights = [15, 3, 2, 5, 9, 20]
values = [15, 7, 10, 5, 8, 17]
capacity = 30
population_size = 50
generations = 100
mutation_rate = 0.1

def initialize_population(population_size, n):
    return [[random.randint(0, 1) for _ in range(n)] for _ in range(population_size)]

def fitness(individual):
    total_weight = sum(weights[i] for i in range(len(individual)) if individual[i])
    total_value = sum(values[i] for i in range(len(individual)) if individual[i])
    if total_weight > capacity:
        return total_value - (total_weight - capacity) * 10
    return total_value


def selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    return random.choices(population, probabilities, k=2)

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutation(individual):
    mutated_individual = individual.copy()
    total_weight = sum(weights[i] for i in range(len(mutated_individual)) if mutated_individual[i])
    while total_weight > capacity:
        idx = random.randint(0, len(mutated_individual) - 1)
        if mutated_individual[idx] == 1:
            mutated_individual[idx] = 0
            total_weight -= weights[idx]
    return mutated_individual


def genetic_algorithm():
    population = initialize_population(population_size, len(names))
    for _ in range(generations):
        fitness_values = [fitness(individual) for individual in population]
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = selection(population, fitness_values)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutation(child1), mutation(child2)])
        population = new_population
    best_individual = max(population, key=fitness)
    return fitness(best_individual), [names[i] for i in range(len(best_individual)) if best_individual[i]]

max_value, items_chosen = genetic_algorithm()

print(f"Valor máximo possível: {max_value}")
print('Itens escolhidos para carregar:')
for item in items_chosen:
    print(item)
