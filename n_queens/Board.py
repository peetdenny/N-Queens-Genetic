from collections import Counter
from math import factorial


class Board:
    """
    Holds the state of the board as a single string of digits, with each digit showing the row position for each column.
    This implementation does not allow more than one Queen to occupy a single column.

    The board is zero indexed with (0,0) in the bottom left-hand corner

    Has a function to return how many conflicting pairs there are.
    """
    def __init__(self, initial_state):
        self.size = len(initial_state)
        if self.size < 4:
            raise ValueError("N-Queens has no solution for board sizes smaller than 4x4. Please try a bigger board")
        for s in initial_state:
            if int(s) >= self.size:
                raise ValueError(
                    "A board of size %s x %s can't contain a row index of value %s" % (self.size, self.size, s))
        self.state = initial_state
        self.eligibility = 0

    def count_attacking_pairs(self):
        # cols - this configuration type doesn't allow attacking within a column, so zero
        # rows - check if the same number appears more than once in config
        counter = dict(Counter(self.state))
        rows = sum(list(map(lambda x: x - 1 if x > 1 else 0, counter.values())))

        # diags - if the horizontal distance == the vertical distance, then they're on the same diagonal.
        diags = 0
        for i in range(self.size-1):
            for j in range(i+1, self.size):
                if abs(i - j) == abs(int(self.state[i]) - int(self.state[j])):
                    diags += 1
        count = rows + diags
        if count is 0:
            print("Found solution to a board of size", self.size, self.state)
            exit()
        return count

    def fitness_function(self):
        return Board.max_attacking_pairs(self.size) - self.count_attacking_pairs()

    def set_eligibility(self, e):
        self.eligibility = e

    def __str__(self):
        return self.state

    @staticmethod
    def max_attacking_pairs(n):
        return factorial(n) / (factorial(n-2) * factorial(2))

    @staticmethod
    def rank_pop(pop):
        pop.sort(key=lambda b: b.eligibility, reverse=True)
        rankings = []
        running_total = 0
        for p in pop:
            running_total += p.eligibility
            rankings.append(running_total)
        return rankings

