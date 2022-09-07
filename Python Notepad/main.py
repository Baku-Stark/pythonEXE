from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("850x550")
root.title("Notepad Python")
root.configure(background="#000000")

# ----------------------------------------
# cores
bg_color = '#111111'
fg_color = '#f0f8ff'

# ----------------------------------------
# função
def salvarComo():
    note = str(fileMenu['label'].get())

    if note == "":
        messagebox.showwarning("AVISO!", "Você precisa digitar algo!")

# ----------------------------------------
# widget
meuMenu = Menu(root)

fileMenu = Menu(meuMenu, tearoff=0)
fileMenu.add_command(label="Novo  - Ctrl + N")
fileMenu.add_command(label="Abrir  - Ctrl + O")
fileMenu.add_command(label="Salvar - Ctrl + S")
fileMenu.add_command(label="Salvar como", command=salvarComo)
fileMenu.add_separator()
fileMenu.add_command(label="Sair")
meuMenu.add_cascade(label="Arquivo", menu=fileMenu)

editMenu = Menu(meuMenu, tearoff=0)
editMenu.add_command(label="Maiúsculo")
editMenu.add_command(label="Minúsculo")
meuMenu.add_cascade(label="Editar", menu=editMenu)

helpMenu = Menu(meuMenu, tearoff=0)
helpMenu.add_command(label="Acessar código do programa")
helpMenu.add_command(label="Autor")
meuMenu.add_cascade(label="Ajuda", menu=helpMenu)
# ----------------------
boxNote = Text(
    root, font=('Arial 10 bold'), bg=bg_color, fg=fg_color
)

# ----------------------------------------
# painel
boxNote.pack()

root.config(menu=meuMenu)
root.mainloop()