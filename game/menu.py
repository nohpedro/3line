import tkinter as tk
from game_ui import TicTacToeGUI  # asume que existe game_ui.py con la clase de la UI del juego

BG_COLOR = "#000000"
FG_COLOR = "#00FF00"
FONT_TITLE = ("Courier", 48, "bold")
FONT_BTN   = ("Courier", 24, "bold")

class StartMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("3 en Raya Retro Pixel")
        self.root.configure(bg=BG_COLOR)
        # Ajustar tamaño ventana para menú
        w = 3*160 + 40
        h = 200
        self.root.geometry(f"{w}x{h}")

        self.frame = tk.Frame(self.root, bg=BG_COLOR)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self._create_widgets()

    def _create_widgets(self):
        title = tk.Label(
            self.frame,
            text="3 en Raya Retro Pixel",
            font=FONT_TITLE,
            bg=BG_COLOR,
            fg=FG_COLOR
        )
        title.pack(pady=(20,10))

        start_btn = tk.Button(
            self.frame,
            text="COMENZAR",
            font=FONT_BTN,
            bg=BG_COLOR,
            fg=FG_COLOR,
            activebackground=BG_COLOR,
            activeforeground=FG_COLOR,
            bd=4,
            relief=tk.RIDGE,
            command=self._on_start
        )
        start_btn.pack(pady=(0,20))

    def show(self):
        """Muestra la pantalla de inicio."""
        self.frame.lift()

    def _on_start(self):
        """Destruye el menú e inicia la UI del juego."""
        self.frame.destroy()
        # Cambiamos el tamaño para el juego
        self.root.geometry(f"{3*160+40}x{3*160+160}")
        TicTacToeGUI(self.root)
