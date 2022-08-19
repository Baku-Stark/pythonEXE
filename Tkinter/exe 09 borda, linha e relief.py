from tkinter import *

janela = Tk()
janela.title("Borda, linhas e relief na lABEL")
janela.geometry("500x300")

label_l = Label(janela, 
    text="Este e o label 1", font=('Arial 20'),
    borderwidth=10, relief="solid")
label_l.pack()
# ==============================================
label_k = Label(janela, 
    text="Este e o label 2", font=('Arial 20'),
    borderwidth=10, relief="groove")
label_k.pack()
# ==============================================
label_j = Label(janela, 
    text="Este e o label 3", font=('Arial 20'),
    borderwidth=10, relief="flat")
label_j.pack()
# ==============================================
label_h = Label(janela, 
    text="Este e o label 4", font=('Arial 20'),
    borderwidth=10, relief="raised")
label_h.pack()
# ==============================================
label_g = Label(janela, 
    text="Este e o label 5", font=('Arial 20'),
    borderwidth=10, relief="sunken")
label_g.pack()
# ==============================================
label_f = Label(janela, 
    text="Este e o label 6", font=('Arial 20'),
    borderwidth=1, relief="ridge")
label_f.pack()


janela.mainloop()