from hex_game import X, O
from hex_game import Board
import unittest


class BoardTest(unittest.TestCase):

    def test_str(self):
        board = Board()
        board.state = [
            [X, O, X],
            [O, None, X],
            [X, X, O]]

        expected = 'x o x \n o _ x \n  x x o \n'
        actual = board.__str__

        self.assertEqual(actual, expected)

    def test_hash(self):
        board = Board()
        board.state = [
            [X, O, X],
            [O, None, X],
            [X, X, O]]

        self.assertEqual(board.hash, board.__str__)

    def test_legal_moves(self):
        board = Board()
        board.state = [
            [X, O, None],
            [O, None, X],
            [X, X, O]]

        expected = [(2, 0), (1, 1)]

        actual = list(board.legal_moves())

        self.assertEquals(actual, expected)

    def test_other_player(self):
        actual = Board.other_player(X)
        expected = O

        self.assertEquals(actual, expected)

        actual = Board.other_player(O)
        expected = X

        self.assertEquals(actual, expected)


class BoardMakeMoveTest(unittest.TestCase):

    def test_make_move(self):
        board = Board()
        board.make_move(1, 2)

        expected = X
        actual = board.state[2][1]

        self.assertEquals(actual, expected)

    def test_active_player_is_toggled(self):
        board = Board()
        board.make_move(0, 0)

        expected = O
        actual = board.active_player

        self.assertEquals(actual, expected)

    def test_make_illegal_move(self):
        board = Board()
        board.state = [
            [X, O, None],
            [O, None, X],
            [X, X, O]]

        with self.assertRaises(Exception):
            board.make_move(0, 0)
