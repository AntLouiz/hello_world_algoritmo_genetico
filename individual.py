from settings import MASTER_SOLUTION


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

    def __repr__(self):
        return "{} Fitness({})".format(self.gene, self.fitness)
