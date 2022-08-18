from tkinter import *

janela = Tk()
janela.title("Centralizar")

# === Dimensão ===
larg = 500
altu = 300

# === Resolução do sistema ===
screen_lar = janela.winfo_screenwidth()
screen_alt = janela.winfo_screenheight()

# === Posição ===
posx = screen_lar / 2 - larg / 2
posy = screen_alt / 2 - altu / 2

# === Geometry ===
janela.geometry(f"{larg}x{altu}+{posx:.0f}+{posy:.0f}")

janela.mainloop()