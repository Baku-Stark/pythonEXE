from tkinter import *

janela = Tk()
janela.title("CHECKBUTTON")

# ----------------------------------------
# função
valor_check = IntVar()

def check():
    print(valor_check.get())

# ----------------------------------------
# widget
check = Checkbutton(
    janela, text="Esta é uma checkbox",
    variable=valor_check, command=check
)
check.pack()


janela.mainloop()