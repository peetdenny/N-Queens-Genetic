from n_queens.Board import Board as Board
import unittest


class TestBoard(unittest.TestCase):

    @staticmethod
    def deep_compare_maps(m1, m2):
        # There's no deep compare built-in to Python 3? o_O
        for key in m1:
            if key not in m2:
                return False
            if len(m2[key]) == 0 and len(m1[key]) == 0:
                continue
            if m2[key][0] is not m1[key][0]:
                return False
        return True

    def test_board_setup(self):
        board = Board("4231")
        assert board.dimensions == (4, 4)
        assert TestBoard.deep_compare_maps(board.rows, {4: [1], 2: [2], 3: [3], 1: [4]})
        assert TestBoard.deep_compare_maps(board.cols, {1: [4], 2: [2], 3: [3], 4: [1]})
        self.assertEqual(board.diagonals['1144'], [2, 3])
        self.assertEqual(board.diagonals['4114'], [1, 4])

        board = Board("12254")
        assert board.dimensions == (5, 5)
        assert TestBoard.deep_compare_maps(board.rows, {1: [1], 2: [2, 3], 4: [5], 5: [4]})
        assert TestBoard.deep_compare_maps(board.cols, {1: [1], 2: [2], 3: [2], 4: [5], 5: [4]})

    def test_count_attacking_pairs(self):
        self.assertEqual(2, Board("1324").count_attacking_pairs())

if __name__ == '__main__':
    unittest.main()