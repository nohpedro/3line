import tkinter as tk
from game_logic import TicTacToe

CELL_SIZE = 100
LINE_WIDTH = 4
MARGIN = 20

class TicTacToeGUI:
    def __init__(self, root):
        self.game = TicTacToe()
        self.root = root
        root.title("3 en Raya - Dos Jugadores")

        # Canvas para tablero y marcas
        self.canvas = tk.Canvas(root, width=3*CELL_SIZE, height=3*CELL_SIZE)
        self.canvas.pack(padx=10, pady=10)
        self.canvas.bind("<Button-1>", self._on_click)

        # Etiqueta de estado y botón de reinicio
        self.status = tk.Label(root, text="Turno de X", font=("Arial", 16))
        self.status.pack()
        self.reset_btn = tk.Button(root, text="Reiniciar", font=("Arial", 12), command=self._on_reset)
        self.reset_btn.pack(pady=(5,10))

        self._draw_grid()

    def _draw_grid(self):
        """Dibuja las líneas del tablero."""
        for i in range(1, 3):
            # líneas verticales
            self.canvas.create_line(i*CELL_SIZE, 0, i*CELL_SIZE, 3*CELL_SIZE, width=LINE_WIDTH)
            # líneas horizontales
            self.canvas.create_line(0, i*CELL_SIZE, 3*CELL_SIZE, i*CELL_SIZE, width=LINE_WIDTH)

    def _on_click(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        result = self.game.make_move(row, col)
        self._redraw_marks()
        if result == "Continue":
            self.status["text"] = f"Turno de {self.game.current_player}"
        elif result == "Invalid":
            self.status["text"] = "Movimiento inválido"
        else:
            self.status["text"] = result
            if result in ("X wins", "O wins"):
                self._draw_win_line(self.game.current_player)

    def _redraw_marks(self):
        """Borra todas las marcas y las vuelve a dibujar."""
        self.canvas.delete("mark")
        for r in range(3):
            for c in range(3):
                mark = self.game.board[r][c]
                x1 = c*CELL_SIZE + MARGIN
                y1 = r*CELL_SIZE + MARGIN
                x2 = (c+1)*CELL_SIZE - MARGIN
                y2 = (r+1)*CELL_SIZE - MARGIN
                if mark == "X":
                    # Dibujar X
                    self.canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, tags="mark")
                    self.canvas.create_line(x1, y2, x2, y1, width=LINE_WIDTH, tags="mark")
                elif mark == "O":
                    # Dibujar O
                    self.canvas.create_oval(x1, y1, x2, y2, width=LINE_WIDTH, tags="mark")

    def _draw_win_line(self, player):
        """Dibuja la línea roja que conecta las 3 en raya."""
        b = self.game.board
        # revisar filas
        for r in range(3):
            if all(b[r][c] == player for c in range(3)):
                y = r*CELL_SIZE + CELL_SIZE/2
                self.canvas.create_line(10, y, 3*CELL_SIZE-10, y, width=LINE_WIDTH*2, fill="red", tags="mark")
                return
        # revisar columnas
        for c in range(3):
            if all(b[r][c] == player for r in range(3)):
                x = c*CELL_SIZE + CELL_SIZE/2
                self.canvas.create_line(x, 10, x, 3*CELL_SIZE-10, width=LINE_WIDTH*2, fill="red", tags="mark")
                return
        # diagonal principal
        if all(b[i][i] == player for i in range(3)):
            self.canvas.create_line(10, 10, 3*CELL_SIZE-10, 3*CELL_SIZE-10,
                                     width=LINE_WIDTH*2, fill="red", tags="mark")
            return
        # diagonal secundaria
        if all(b[i][2-i] == player for i in range(3)):
            self.canvas.create_line(10, 3*CELL_SIZE-10, 3*CELL_SIZE-10, 10,
                                     width=LINE_WIDTH*2, fill="red", tags="mark")
            return

    def _on_reset(self):
        self.game.reset()
        self.canvas.delete("all")
        self._draw_grid()
        self.status["text"] = f"Turno de {self.game.current_player}"

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToeGUI(root)
    root.mainloop()
