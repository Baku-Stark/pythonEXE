from tkinter import *

janela = Tk()
janela.title("SPINBOX")
janela.geometry("300x200")

# ----------------------------------------
# função
def executar():
    print('-' *15)
    print(spin1.get())
    print(spin2.get())
    print(spin3.get())
    print('-' *15)
    print('')

# ----------------------------------------
# widget
spin1 = Spinbox(
    janela, from_ = 0, to = 10
)


# ----- Valores especificos
spin2 = Spinbox(
    janela, values = (10, 20, 30, 40, 50)
)


# ----- Valores com STRING
spin3 = Spinbox(
    janela, values = ("Tony", "Natasha", "Thor")
)

cmd = Button(
    janela, text="Click!", command=executar
)

# ----------------------------------------
# painel
spin1.pack()
spin2.pack()
spin3.pack()
cmd.pack()


janela.mainloop()