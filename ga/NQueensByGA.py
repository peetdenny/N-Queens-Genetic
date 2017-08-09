import random
from n_queens.Board import Board as Board

board_size = 6
population_size = 10
no_of_parents = 4  # should be an even number, and I can't be razzed to put in a proper check
children_per_parent = 2
attempts = 20000


def generate_board(length):
    s = ""
    for _ in range(length):
        s += str(random.randint(0, length-1))
    return Board(s)


def print_population(population):
    for p in population:
        print("Board %s has %s attacking pairs" % (p, p.count_attacking_pairs()))


def gen_population():
    population = []
    for _ in range(population_size):
        population.append(generate_board(board_size))
    return population


def get_parents(rankings, population):
    """ Selects the top n parents based on n random dice throws"""
    parents = []
    for i in range(no_of_parents):
        r = random.random()
        idx = 0
        while r > rankings[idx]:
            idx += 1
        parents.append(population[idx])
    return parents


def get_rankings(population):
    """
    Takes a population and ranks it from the most eligible parents to the least
    """
    total_attacking_pairs = sum(map(lambda x: x.fitness_function(), population))
    for board in population:
        board.set_eligibility(board.fitness_function() / total_attacking_pairs)
    return Board.rank_pop(population)


def make_babies(p1, p2, pivot):
    k1_state = p1[0:pivot] + p2[pivot:]
    k2_state = p2[0:pivot] + p1[pivot:]

    k1 = Board(k1_state)
    k2 = Board(k2_state)
    return k1, k2


def breed(parents):
    idx = 0
    kids = []
    while idx < len(parents) - 1:
        p1 = parents[idx].state
        p2 = parents[idx + 1].state
        assert len(p1) == len(p2)  # sanity check
        pivot = random.randint(0, len(p1))
        k1, k2 = make_babies(p1, p2, pivot)
        kids.append(k1)
        kids.append(k2)
        idx += 2  # dangerous, unverified assumptions abound!
    return kids


def find_solution():
    attempt = 0
    population = gen_population()
    while attempt < attempts:
        rankings = get_rankings(population)
        parents = get_parents(rankings, population)
        population = breed(parents)
        print("new population", *population)
        attempt += 1
    print("ran %s attempts, now exiting" % attempt)

if __name__ == '__main__':
    find_solution()