from settings import (
    INITIAL_POPULATION,
    MASTER_SOLUTION,
    MAX_ITERATIONS
)
from utils import (
    generate_individual,
    tournament_selection,
    crossover,
    mutate_population
)


def main():
    population = []
    generation = 1

    for i in range(INITIAL_POPULATION):
        population.append(
            generate_individual(len(MASTER_SOLUTION))
        )

    while generation < MAX_ITERATIONS:
        print("Generation: {}, Population: {}".format(generation, len(population)))
        new_population = tournament_selection(population)

        population = []
        for x, y in new_population:
            population.append(crossover(x, y))
            population.append(crossover(y, x))

        population = mutate_population(population)

        generation += 1


if __name__ == '__main__':
    main()
