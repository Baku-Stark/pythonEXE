from tkinter import *

janela = Tk()
janela.geometry("300x200")
janela.title("ADICIONAR MENUS À APLICAÇÃO")

# ----------------------------------------
# função
def file():
    print('File selecionado.')
def fileNew_click():
    print('Novo Arquivo')

def edit():
    print('Edit selecionado.')

# ----------------------------------------
# widget
meuMenu = Menu(janela)

# ---------- File Menu
fileMenu = Menu(meuMenu, tearoff=1)
fileMenu.add_command(label="New", command=fileNew_click)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_separator()
fileMenu.add_command(label="Open File")
meuMenu.add_cascade(label="File", menu=fileMenu, command=file)

# ---------- Edit Menu
editMenu = Menu(meuMenu, tearoff=0)
editMenu.add_command(label="Undo   Ctrl+Z")
editMenu.add_command(label="Redo   Ctrl+Y")
editMenu.add_separator()
editMenu.add_command(label="Cut     Ctrl+X")
editMenu.add_command(label="Copy    Ctrl+C")
editMenu.add_command(label="Paste    Ctrl+V")
meuMenu.add_cascade(label="Edit", menu=editMenu, command=edit)


janela.config(menu=meuMenu)
janela.mainloop()