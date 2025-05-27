# unit_test/test_tdd.py

import unittest
from game.game_logic import TicTacToe


class TestTDDTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_x_out_of_bounds_returns_invalid(self):
        self.assertEqual(self.game.make_move(-1, 0), "Invalid")
        self.assertEqual(self.game.make_move(3, 0), "Invalid")

    def test_y_out_of_bounds_returns_invalid(self):
        self.assertEqual(self.game.make_move(0, -1), "Invalid")
        self.assertEqual(self.game.make_move(0, 3), "Invalid")

        
    def test_first_turn_is_X(self):
        self.assertEqual(self.game.current_player, "X")

    def test_next_turn_after_X_is_O(self):
        self.game.make_move(0, 0)
        self.assertEqual(self.game.current_player, "O")

    def test_next_turn_after_O_is_X(self):
        self.game.make_move(0, 0)
        self.game.make_move(0, 1)
        self.assertEqual(self.game.current_player, "X")

    def test_no_winner_initially(self):
        self.assertIsNone(self.game.winner)

if __name__ == "__main__":
    unittest.main()
