class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None

    def make_move(self, row: int, col: int) -> str:
        if self.winner:
            return "GameOver"
        if not (0 <= row < 3 and 0 <= col < 3):
            return "Invalid"
        if self.board[row][col] != "":
            return "Invalid"

        self.board[row][col] = self.current_player
        if self._check_winner(row, col):
            self.winner = self.current_player
            return f"{self.current_player} wins"
        if self._is_draw():
            self.winner = "Draw"
            return "Draw"

        self.current_player = "O" if self.current_player == "X" else "X"
        return "Continue"

    def _check_winner(self, row: int, col: int) -> bool:
        b = self.board
        p = self.current_player

        # Fila
        if all(b[row][c] == p for c in range(3)):
            return True
        # Columna
        if all(b[r][col] == p for r in range(3)):
            return True
        # Diagonal principal
        if row == col and all(b[i][i] == p for i in range(3)):
            return True
        # Diagonal secundaria
        if row + col == 2 and all(b[i][2 - i] == p for i in range(3)):
            return True

        return False

    def _is_draw(self) -> bool:
        return all(cell != "" for row in self.board for cell in row)
