from tkinter import *

janela = Tk()
janela.title("SCALE")
janela.geometry("300x300")

# ----------------------------------------
# função
def valor(v):
    print(v)

def valor_sec():
    print(slide2.get())

# ----------------------------------------
# widget
slide = Scale(
    janela, from_ = 0, to = 100, orient=VERTICAL, command=valor
)
slide2 = Scale(
    janela, from_ = 0, to = 100, orient=HORIZONTAL, resolution = 0.5
)

cmd = Button(
    janela, text="Ver valor do scale 2", command=valor_sec
)

# ----------------------------------------
# painel
slide.pack()
slide2.pack()

cmd.pack()


janela.mainloop()