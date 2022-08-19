from tkinter import *

janela = Tk()
janela.title("Alterar Cor E Fonte")
janela.geometry("500x300")

label_l = Label(janela, 
                text="Este é o label 1", font=('Arial 20 bold'), bg="#111111", fg="#0000ff")
label_l.pack()
# =======================
label_k = Label(janela, 
                text="Este é o label 2", font=('Impact 20 bold'), bg="#0000ff", fg="#111111")
label_k.pack()
# =======================
label_j = Label(janela, 
                text="Este é o label 3", font=('Helvetica 20 bold'), bg="#80ffff", fg="#111111")
label_j.pack()
# =======================
label_h = Label(janela, 
                text="Este é o label 4", font=('Times 20 bold'), bg="#111111", fg="#80ffff")
label_h.pack()


janela.mainloop()