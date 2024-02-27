import random

names = ["Saco de dormir", "Corda", "Canivete", "Tocha", "Garrafa", "Comida"]
values = [15, 7, 10, 5, 8, 17]
weights = [15, 3, 2, 5, 9, 20]
capacity = 30
population_size = 100
generations = 50
mutation_rate = 0.1

def calculate_fitness(individual, values, weights, capacity):
    weight = sum(w * i for w, i in zip(weights, individual))
    value = sum(v * i for v, i in zip(values, individual))
    if weight > capacity:
        return -1
    else:
        return value


def estimate_distribution(population):
    length = len(population[0])
    distribution = [sum(individual[i] for individual in population) / len(population) for i in range(length)]
    return distribution


def generate_individual_with_distribution(distribution):
    new_individual = [1 if random.random() < gene_prob else 0 for gene_prob in distribution]
    return new_individual


def mutate(individual, mutation_rate):
    return [gene if random.random() > mutation_rate else 1 - gene for gene in individual]


def select_parents(population, fitnesses, num_parents):
    selected_indices = sorted(range(len(fitnesses)), key=lambda i: fitnesses[i], reverse=True)[:num_parents]
    return [population[i] for i in selected_indices]


def genetic_algorithm(names, values, weights, capacity, population_size=population_size, generations=generations, mutation_rate=mutation_rate,
                      num_parents=50):
    population = [[random.randint(0, 1) for _ in range(len(values))] for _ in range(population_size)]

    for generation in range(generations):
        fitnesses = [calculate_fitness(ind, values, weights, capacity) for ind in population]

        parents = select_parents(population, fitnesses, num_parents)
        distribution = estimate_distribution(parents)

        new_population = [generate_individual_with_distribution(distribution) for _ in
                          range(population_size - len(parents))]
        new_population += parents

        new_population = [mutate(ind, mutation_rate) for ind in new_population]

        population = new_population

    final_fitnesses = [calculate_fitness(ind, values, weights, capacity) for ind in population]
    best_index = final_fitnesses.index(max(final_fitnesses))
    best_individual = population[best_index]

    print("Melhor indivíduo:", best_individual)
    print("Itens escolhidos:", [names[i] for i in range(len(best_individual)) if best_individual[i] == 1])
    print("Valor total:", calculate_fitness(best_individual, values, weights, capacity))

genetic_algorithm(names, values, weights, capacity)