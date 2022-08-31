from tkinter import *

janela = Tk()
janela.title("RADIOBUTTON")

valor_a = IntVar()

# ----------------------------------------
# função
def select():
    print(valor_a.get())

def opcA():
    print("Opção 1 selecionada.")

# ----------------------------------------
# widget
ra_a = Radiobutton(
    janela, text="Opção A1", variable=valor_a, value=1, command=opcA
)
ra_b = Radiobutton(
    janela, text="Opção A2", variable=valor_a, value=2, indicatoron=0
)
ra_c = Radiobutton(
    janela, text="Opção A3", variable=valor_a, value=3
)
cmd = Button(
    janela, text="Ver opção", command=select
)

# ----------------------------------------
# painel
ra_a.pack()
ra_b.pack()
ra_c.pack()
cmd.pack()


janela.mainloop()