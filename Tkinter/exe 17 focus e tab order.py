from tkinter import *

janela = Tk()
janela.title("FOCUS E TAB ORDER")

# ----------------------------------------
# função
def executar():
    label_l['text'] = t1.get()
    label_k['text'] = t2.get()
    label_j['text'] = t3.get()

# ----------------------------------------
# widget
t1 = Entry(janela)
t2 = Entry(janela)
t3 = Entry(janela)

label_l = Label(janela)
label_k = Label(janela)
label_j = Label(janela)
btn = Button(janela, text="Executar", command=executar)

# ----------------------------------------
# layout
t1.grid()
t2.grid()
t3.grid()

t1.focus() #cursor vai estar na caixa de texto 1

label_l.grid()
label_k.grid()
label_j.grid()
btn.grid()


janela.mainloop()