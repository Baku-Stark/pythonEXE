from tkinter import *


janela = Tk()
janela.geometry("300x200")
janela.title("CRIAR EXECUTÁVEL COM O PYINSTALLER")

# ----------------------------------------
# função
texto = StringVar()
texto.set("")

def executar():
    texto.set('Texto alterado')

# ----------------------------------------
# widget
label_1 = Label(
    janela, textvariable=texto
)

cmd = Button(
    janela, command=executar, text="Executar"
)

# ----------------------------------------
# painel
label_1.pack()
cmd.pack()

janela.mainloop()