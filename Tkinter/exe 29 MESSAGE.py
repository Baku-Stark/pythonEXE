from tkinter import *

janela = Tk()
janela.title("MESSAGE")

# ----------------------------------------
# widget
t = Message(
    janela, text="Este é o texto do widget MESSAGE.",
    width=200
)

# ----------------------------------------
# painel
t.pack()


janela.mainloop()