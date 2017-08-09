import unittest
import ga.NQueensByGA as NQ
from n_queens.Board import Board


class TestNQueens(unittest.TestCase):

    def setUp(self):
        p1 = Board("222222")
        p2 = Board("555555")
        p3 = Board("222222")
        p4 = Board("555555")
        self.short_list = [p1, p2]
        self.long_list = [p1, p2, p3, p4]

    def test_breed(self):
        kids = NQ.breed(self.short_list)
        self.assertEqual(2, len(kids))  # 2 kids per pair of parents

        kids = NQ.breed(self.long_list)
        self.assertEqual(4, len(kids))

    def test_make_babies(self):
        p1 = self.short_list[0].state
        p2 = self.short_list[1].state
        pivot = 3
        kids = NQ.make_babies(p1, p2, pivot)
        self.assertEqual(kids[0].state, "222555")
        self.assertEqual(kids[1].state, "555222")

        pivot = 1
        kids = NQ.make_babies(p1, p2, pivot)
        self.assertEqual(kids[0].state, "255555")
        self.assertEqual(kids[1].state, "522222")

