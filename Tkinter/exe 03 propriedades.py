from tkinter import *

janela = Tk()
janela.title("Primeira Aplicação")
janela.geometry("500x250")

# ----- Background
janela['bg'] = "#111111"

# ----- Botão
btn = Button(janela, text="Botão De Click")
# ----- Posição da propiedade
btn.place(x=0, y=0)

janela.mainloop()