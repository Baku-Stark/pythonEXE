from tkinter import *

janela = Tk()
janela.title("COLUMNSPAN EM GRID")

Label(
    janela, text="Texto Red", width=20, bg="red"
).grid(column=0)

Label(
    janela, text="Texto Green", width=20, bg="green"
).grid(column=1)

Label(
    janela, text="Texto Blue", width=40, bg="blue"
).grid(columnspan=2, sticky='we')

janela.mainloop()