from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

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
def novo():
    print('\033[1;34mNovo Arquivo\033[m')

    with open("Novo Arquivo.txt", "a") as arquivo:
        text = boxNote.get(0.0, END)
        arquivo.write(text.rstrip())

def abrir():
    print('\033[1;34mAbrir Arquivo\033[m')
    
    noteOpen = filedialog.askopenfile(mode='r+', defaultextension=".txt")
    text = boxNote.get(0.0, END)
    noteOpen.write(text.rstrip())

def salvar():
    print('\033[1;34mSalvar\033[m')

    note = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    text = boxNote.get(0.0, END)
    note.write(text.rstrip())

def salvarComo():
    print('\033[1;34mSalvar Como\033[m')
    
    note = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    text = boxNote.get(0.0, END)
    note.write(text.rstrip())

# ----------------------------------------
# widget
meuMenu = Menu(root)

fileMenu = Menu(meuMenu, tearoff=0)
fileMenu.add_command(label="Novo  - Ctrl + N", command=novo)
fileMenu.add_command(label="Abrir  - Ctrl + O", command=abrir)
fileMenu.add_command(label="Salvar - Ctrl + S", command=salvar)
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

scroll = Scrollbar(
    root
)
scroll.config(command=boxNote.yview)
boxNote.config(yscrollcommand=scroll.set)

# ----------------------------------------
# painel
boxNote.pack(side=LEFT, expand=True)
scroll.pack(side=RIGHT, fill=Y)

root.config(menu=meuMenu)
root.mainloop()