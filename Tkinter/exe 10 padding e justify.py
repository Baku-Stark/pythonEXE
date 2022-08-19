from tkinter import *

janela = Tk()
janela.title("Padding e Justify")
janela.geometry("500x300")

label_l = Label(janela, text="Frase teste", font=('Arial 20'), anchor=W,
    bd=1, relief="solid", width=25, height=2)
label_l.pack()


janela.mainloop()