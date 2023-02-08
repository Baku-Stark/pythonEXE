from tkinter import *

janela = Tk()
janela.title("ADICIONAR IMAGEM A UM LAYOUT")

# ----------------------------------------
# widgget
img = PhotoImage(file=("imagens/runa-icon.png"))

label_imagem = Label(
    janela,
    image=img
)
label_imagem.pack()


janela.mainloop()