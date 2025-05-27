import unittest
from game.game_logic import TicTacToe

class TestTicTacToeLogic(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_initial_state(self):
        self.assertEqual(self.game.current_player, "X")
        self.assertEqual(self.game.board, [["", "", ""]]*3)
        self.assertIsNone(self.game.winner)

    def test_invalid_move_on_taken_cell(self):
        self.game.make_move(1, 1)
        self.assertEqual(self.game.make_move(1, 1), "Invalid")

    def test_row_win(self):
        self.game.make_move(0, 0)  # X
        self.game.make_move(1, 0)  # O
        self.game.make_move(0, 1)  # X
        self.game.make_move(1, 1)  # O
        self.assertEqual(self.game.make_move(0, 2), "X wins")
        self.assertEqual(self.game.winner, "X")

    def test_column_win(self):
        self.game.current_player = "O"
        self.game.make_move(0, 2)  # O
        self.game.make_move(0, 0)  # X
        self.game.make_move(1, 2)  # O
        self.game.make_move(1, 0)  # X
        self.assertEqual(self.game.make_move(2, 2), "O wins")
        self.assertEqual(self.game.winner, "O")

    def test_diagonal_win(self):
        self.game.make_move(0, 0)
        self.game.make_move(0, 1)
        self.game.make_move(1, 1)
        self.game.make_move(0, 2)
        self.assertEqual(self.game.make_move(2, 2), "X wins")
        self.assertEqual(self.game.winner, "X")

    def test_draw(self):
        moves = [
            (0,0),(0,1),(0,2),
            (1,1),(1,0),(1,2),
            (2,1),(2,0),(2,2)
        ]
        results = []
        for move in moves:
            results.append(self.game.make_move(*move))
        self.assertEqual(results[-1], "Draw")
        self.assertEqual(self.game.winner, "Draw")

    def test_gameover_after_win(self):
        self.test_row_win()
        self.assertEqual(self.game.make_move(2, 2), "GameOver")

if __name__ == "__main__":
    unittest.main()
