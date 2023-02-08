from tkinter import *

janela = Tk()
janela.title("PADDING E JUSTIFICAÇÃO DE TEXTO NUM LABEL")
janela.geometry("500x500")

label_l = Label(janela, text="Frase de Teste", font=('Aria 20'), bd=1, relief="solid", padx=50, pady=50)
label_l.pack()

label_k = Label(
    janela, 
    text="Frase de Teste\nOutra frase\nMais outra frase",
    font=('Aria 10'),
    bd=1,
    relief="solid",
    justify=RIGHT
)
label_k.pack()

label_j = Label(
    janela, 
    text="Frase de Teste2\n Teste Teste Teste",
    font=('Aria 10'),
    bd=1,
    relief="solid",
    width=30,
    height=5,
    justify=LEFT,
    anchor=W
)
label_j.pack()


janela.mainloop()