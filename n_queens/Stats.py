import sys


class Stats:
    population_strength = 0
    best_fitness_score = 0
    fittest_individual = None
    record_number = 0
    max_fitness = float("inf")
    reporting_granularity = 10000

    def __init__(self, board_size, max_fitness):
        self.max_fitness = int(max_fitness)
        self.board_size = board_size

    def record(self, population):
        self.record_number += 1
        population_fitness = 0
        for b in population:
            fitness = b.fitness
            if fitness == self.max_fitness:
                print("Found solution to a board of size %s after %s generations: %s" %
                      (b.size, self.record_number, b.state))
                exit()
            population_fitness += b.fitness
            if self.best_fitness_score < fitness:
                self.best_fitness_score = fitness
                self.fittest_individual = b
        if self.record_number % self.reporting_granularity == 0:
            self.report(population)

    def report(self, population):
        print("new population {} \r", *population)
        print("Fittest Individual {:^10} with a score of {:^4} \r"
                         .format(self.fittest_individual.state, self.best_fitness_score))
