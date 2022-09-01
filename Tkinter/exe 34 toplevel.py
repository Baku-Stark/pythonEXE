from tkinter import *

janela = Tk()
janela.title("TOPLEVEL")

# ----------------------------------------
# função
def abrir_formulario():
    top = Toplevel()
    top.geometry("200x100")
    top.title("Novo Formulário")

    label1 = Label(
    top, text="Label na nova janela."
    )
    
    label1.pack()

# ----------------------------------------
# widget
btn = Button(
    janela, text="Novo...", command=abrir_formulario
)
# ----------------------------------------
# painel
btn.pack()


janela.mainloop()