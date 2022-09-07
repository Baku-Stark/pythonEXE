from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x500")
root.title("Notepad Python")
root.configure(background='#000000')
root.resizable(width=FALSE, height=FALSE)

# ----------------------------------------
# cores
bg_label = '#111111'
btn = '#2C00A3'
fg = '#f0f8ff'

# ----------------------------------------
# função
def anotar():
    note = str(note_bar.get())
    if note == "":
        messagebox.showwarning('AVISO!', 'VOCÊ PRECISA ESCREVER ALO PRIMEIRO.')
    else:
        with open("Notepad Python.txt", 'w') as notepad:
            notepad.write(note)
    for i in note:
        label_note.insert(END, i)
# ----------------------------------------
# widget
note_bar = Entry(
    root, font=('Arial 15')
)

btn = Button(
    root, text='Anotar!', command=anotar, font=('Arial 10 bold'), width=27,
    bg=btn, relief=RAISED, overrelief=RIDGE
)

label_note = Listbox(
    root, bg=bg_label, font=('Arial 9'), fg=fg,
    width=39, height=26
)

scroll = Scrollbar(
    root, 
)
scroll.config(command=label_note.yview)

# ----------------------------------------
# painel
note_bar.grid(row=0, column=0)
btn.grid(row=1, column=0)
label_note.place(x=1, y=78)
scroll.place(x=280, y=78)

root.mainloop()