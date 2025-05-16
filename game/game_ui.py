# game_ui.py

import tkinter as tk
from game_logic import TicTacToe

# Estilos retro-pixel
BG_COLOR        = "#000000"  # fondo negro
FG_COLOR        = "#00FF00"  # verde neón
BTN_BG          = "#111111"  # botón fondo oscuro
BTN_ACTIVE_BG   = "#003300"  # botón activo verde oscuro
WIN_BTN_BG      = "#FF0000"  # botón victoria rojo
FONT_MARK       = ("Courier", 48, "bold")  # fuente monoespaciada grande

class TicTacToeGUI:
    def __init__(self, root):
        self.game = TicTacToe()
        self.root = root
        self.root.title("3 en Raya Retro Pixel")
        self.root.configure(bg=BG_COLOR)
        self._create_widgets()

    def _create_widgets(self):
        # Marco del tablero
        board_frame = tk.Frame(self.root, bg=BG_COLOR)
        board_frame.pack(pady=20)

        # Botones 3×3
        self.buttons = []
        for r in range(3):
            row = []
            for c in range(3):
                btn = tk.Button(
                    board_frame,
                    text="",
                    font=FONT_MARK,
                    width=4,
                    height=2,
                    bg=BTN_BG,
                    fg=FG_COLOR,
                    activebackground=BTN_ACTIVE_BG,
                    activeforeground=FG_COLOR,
                    bd=4,
                    relief=tk.RIDGE,
                    command=lambda r=r, c=c: self._on_click(r, c)
                )
                btn.grid(row=r, column=c, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

        # Etiqueta de estado
        self.status = tk.Label(
            self.root,
            text="Turno de X",
            font=("Courier", 24, "bold"),
            bg=BG_COLOR,
            fg=FG_COLOR
        )
        self.status.pack(pady=(0, 10))

        # Botón de reiniciar
        self.reset_btn = tk.Button(
            self.root,
            text="REINICIAR",
            font=("Courier", 18, "bold"),
            bg=BG_COLOR,
            fg=FG_COLOR,
            activebackground=BG_COLOR,
            activeforeground=FG_COLOR,
            bd=4,
            relief=tk.RIDGE,
            command=self._on_reset
        )
        self.reset_btn.pack(pady=(0, 20))

    def _on_click(self, row: int, col: int):
        result = self.game.make_move(row, col)
        self._update_buttons()
        if result == "Continue":
            self.status["text"] = f"Turno de {self.game.current_player}"
        elif result == "Invalid":
            self.status["text"] = "Movimiento inválido"
        else:
            # "X wins", "O wins" o "Draw"
            self.status["text"] = result
            if result.endswith("wins"):
                self._highlight_win(self.game.current_player)
            self._disable_all()

    def _update_buttons(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c]["text"] = self.game.board[r][c]

    def _highlight_win(self, player: str):
        b = self.game.board
        # Filas
        for r in range(3):
            if all(b[r][c] == player for c in range(3)):
                for c in range(3):
                    self.buttons[r][c].configure(bg=WIN_BTN_BG)
                return
        # Columnas
        for c in range(3):
            if all(b[r][c] == player for r in range(3)):
                for r in range(3):
                    self.buttons[r][c].configure(bg=WIN_BTN_BG)
                return
        # Diagonal principal
        if all(b[i][i] == player for i in range(3)):
            for i in range(3):
                self.buttons[i][i].configure(bg=WIN_BTN_BG)
            return
        # Diagonal secundaria
        if all(b[i][2 - i] == player for i in range(3)):
            for i in range(3):
                self.buttons[i][2 - i].configure(bg=WIN_BTN_BG)
            return

    def _disable_all(self):
        for row in self.buttons:
            for btn in row:
                btn.configure(state=tk.DISABLED)

    def _on_reset(self):
        self.game.reset()
        for row in self.buttons:
            for btn in row:
                btn.configure(text="", state=tk.NORMAL, bg=BTN_BG)
        self.status["text"] = f"Turno de {self.game.current_player}"
