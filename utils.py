import sys
from random import randint
from settings import ALPHABET, MASTER_SOLUTION, INITIAL_POPULATION
from individual import Individual
from operator import attrgetter


def generate_individual(max_length):
    gene = ''
    for i in range(max_length):
        gene += ALPHABET[randint(0, len(ALPHABET) - 1)]

    return Individual(gene)


def tournament_selection(population):
    selected_candidates = []

    for x in population:
        arena = [population[randint(0, len(population) - 1)] for i in range(2)]
        best = max(arena, key=attrgetter('fitness'))
        # print(best)

        if(best.fitness == 11):
            print("ENCONTREI A MELHOR SOLUCAO: {}".format(best.gene))
            sys.exit()

        selected_candidates.append(best)

    return zip(selected_candidates, selected_candidates[int(len(selected_candidates) / 2):])


def crossover(first_individual, second_individual):
    binary_mask = [randint(0, 1) for i in range(len(MASTER_SOLUTION))]
    son = ''

    for i in range(len(binary_mask)):
        if binary_mask[i]:
            son += first_individual.gene[i]
        else:
            son += second_individual.gene[i]

    return Individual(son)


def mutate_population(population):
    mutate_percentual = 5
    total_mutations = int((INITIAL_POPULATION * mutate_percentual) / 100)

    for i in range(total_mutations):
        population[randint(0, len(population) - 1)].mutate()

    return population
