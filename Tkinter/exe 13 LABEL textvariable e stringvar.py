from tkinter import *

red = "#ed1405"
white = "#ffffff"

janela = Tk()
janela.title("LABEL TEXTVARIABLE E STRINGVAR")
janela.geometry("500x500")

label_l = Label(
    janela,
    text="palavra",
    font=('Arial 20'),
    bg=red,
    fg=white)
label_l.pack()

label_l['text'] = "Olá, Mundo!"

# ===============================================
texto = StringVar()
texto.set("Novo Texto")

label_k = Label(
    janela,
    textvariable=texto,
    font=('Arial 20'),
    bg=red,
    fg=white)
label_k.pack()

janela.mainloop()