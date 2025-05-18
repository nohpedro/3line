# unit_test/test_tdd_kata.py

import unittest
from game.game_logic import TicTacToe

class TestTDDTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    # Requerimiento 1: Validación de posición
    def test_x_out_of_bounds_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.game.make_move(-1, 0)
        with self.assertRaises(IndexError):
            self.game.make_move(3, 0)

    def test_y_out_of_bounds_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.game.make_move(0, -1)
        with self.assertRaises(IndexError):
            self.game.make_move(0, 3)

    def test_move_on_occupied_cell_raises_value_error(self):
        self.game.make_move(1, 1)        # X ocupa (1,1)
        with self.assertRaises(ValueError):
            self.game.make_move(1, 1)    # intentar de nuevo sobre (1,1)

    # Requerimiento 2: Turnos alternos
    def test_first_turn_is_X(self):
        self.assertEqual(self.game.current_player, "X")

    def test_next_turn_after_X_is_O(self):
        self.game.make_move(0, 0)  # X
        self.assertEqual(self.game.current_player, "O")

    def test_next_turn_after_O_is_X(self):
        self.game.make_move(0, 0)  # X
        self.game.make_move(0, 1)  # O
        self.assertEqual(self.game.current_player, "X")

    # Requerimiento 3: Detección de ganador
    def test_no_winner_initially(self):
        self.assertIsNone(self.game.winner)

    def test_horizontal_win(self):
        # X completa fila 0
        self.game.make_move(0, 0)  # X
        self.game.make_move(1, 0)  # O
        self.game.make_move(0, 1)  # X
        self.game.make_move(1, 1)  # O
        result = self.game.make_move(0, 2)  # X completa línea
        self.assertEqual(result, "X wins")
        self.assertEqual(self.game.winner, "X")

    def test_vertical_win(self):
        # O completa columna 2
        self.game.current_player = "O"
        self.game.make_move(0, 2)  # O
        self.game.make_move(0, 0)  # X
        self.game.make_move(1, 2)  # O
        self.game.make_move(1, 0)  # X
        result = self.game.make_move(2, 2)  # O completa línea
        self.assertEqual(result, "O wins")
        self.assertEqual(self.game.winner, "O")

    def test_diagonal_win(self):
        # X completa diagonal principal
        self.game.make_move(0, 0)  # X
        self.game.make_move(0, 1)  # O
        self.game.make_move(1, 1)  # X
        self.game.make_move(0, 2)  # O
        result = self.game.make_move(2, 2)  # X completa diagonal
        self.assertEqual(result, "X wins")
        self.assertEqual(self.game.winner, "X")

if __name__ == "__main__":
    unittest.main()


#prueba