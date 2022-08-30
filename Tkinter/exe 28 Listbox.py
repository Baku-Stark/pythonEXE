from tkinter import *

janela = Tk()
janela.title("LISTBOX")

# ----------------------------------------
# função
def Executar():
    print(lista.get(ACTIVE))

# ----------------------------------------
# widget
lista = Listbox(
    janela, selectmode=EXTENDED
)

cmd = Button(
    janela, text="Clique", command=Executar
)

lista.pack()
cmd.pack()

# ----------------------------------------
# Itens (lista)
# ----- Formato por Números
lista.insert(0, "Primeiro Item da lista")
lista.insert(1, "Segundo Item da lista")

# ----- Método END
lista.insert(END, "Primeiro Item da lista (END)")
lista.insert(END, "Segundo Item da lista (END)")

# ----------------------------------------
# Vários Itens (lista)
nomes = ['Wallace', 'Bruce', 'Tony']
for nome in nomes:
    lista.insert(END, nome)

lista.delete(1, 1) #--- Apagar item da lista
janela.mainloop()