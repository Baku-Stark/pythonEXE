from tkinter import *

janela = Tk()
janela.title("Primeira Aplicação")

# ----- dimensão da janela(largura, altura)
janela.geometry("500x250")
# ----- redimensionar janela (Horizontal, Vertical)
janela.resizable(True, True)
# ----- Tamanho MÍNIMO e MÁXIMO
janela.minsize(width=500, height=250)
janela.maxsize(width=700, height=400)

janela.mainloop()