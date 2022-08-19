from tkinter import *

janela = Tk()
janela.title("Largura de Label")

label_l = Label(janela, text="Este é o label 1", bg="red", width=50)
label_l.pack()

janela.mainloop()