from random import randint
from settings import MASTER_SOLUTION, ALPHABET


class Individual(object):

    def __init__(self, gene, grade=None):
        self.gene = gene
        self.grade = grade
        self.sons = []

    def copulate(self, patner):
        pass

    @property
    def fitness(self):
        fitness_value = 0

        for i in range(len(MASTER_SOLUTION)):
            if self.gene[i] == MASTER_SOLUTION[i]:
                fitness_value += 1

        return fitness_value

    def mutate(self):
        new_gene = []
        random_gene_index = randint(0, len(self.gene) - 1)

        for i in range(len(self.gene)):
            gene = self.gene[i]

            if i == random_gene_index:
                gene = ALPHABET[randint(0, len(ALPHABET) - 1)]

            new_gene.append(gene)

        self.gene = ''.join(new_gene)

    def __repr__(self):
        return "{} -- Fitness({})".format(self.gene, self.fitness)
