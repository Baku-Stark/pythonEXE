from tkinter import *

janela = Tk()
janela.title("Label Widget")
janela.geometry("500x300")

# === LABEL ===
label_l = Label(janela, text="Este é o label 1")
label_l.pack()

label_k = Label(janela, text="Este é o label 2")
label_k.pack()

label_j = Label(janela, text="Este é o label 3")
label_j.pack()

cmd = Button(janela, text="Executar")
cmd.pack()

janela.mainloop()