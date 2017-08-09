from n_queens.Board import Board as Board
import unittest


class TestBoard(unittest.TestCase):

    def test_consistency_check(self):
        with self.assertRaises(ValueError):
            Board("0126")  # row index is higher than is possible for a 4x4 board

        with self.assertRaises(ValueError):
            Board("012")  # No solution for N-Queens len() < 4

    def test_count_attacking_pairs(self):
        self.assertEqual(2, Board("0213").count_attacking_pairs())
        self.assertEqual(2, Board("3120").count_attacking_pairs())
        self.assertEqual(4, Board("01143").count_attacking_pairs())
        self.assertEqual(4, Board("02143").count_attacking_pairs())

    def test_calc_max_attacking_pairs(self):
        self.assertEqual(28, Board.max_attacking_pairs(8))
        self.assertEqual(15, Board.max_attacking_pairs(6))
        self.assertEqual(120, Board.max_attacking_pairs(16))

    def test_fitness_function(self):
        self.assertEqual(4, Board("0213").fitness_function())

    def test_sorting_by_eligibility(self):
        a = Board("0213")
        b = Board("3120")
        c = Board("0101")
        a.set_eligibility(0.2)
        b.set_eligibility(0.7)
        c.set_eligibility(0.1)
        pop = [a, b, c]
        print(pop)
        Board.rank_pop(pop)
        print(pop)
        self.assertIs(pop[0], b)
        self.assertIs(pop[1], a)
        self.assertIs(pop[2], c)


if __name__ == '__main__':
    unittest.main()
