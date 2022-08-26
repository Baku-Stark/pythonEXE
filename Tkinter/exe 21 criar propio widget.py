from tkinter import *

janela = Tk()
janela.title("CRIAR O NOSSO WIDGET")

# ----------------------------------------
# widget
class FrameNome(Frame):
    def __init__(self, master):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID

        label_nome = Label(self, text="Nome: ")
        text_nome = Entry(self)

        label_nome.grid(row=0, column=0)
        text_nome.grid(row=0, column=1)

# ----------------------------------------
# GUI
frame_nome1 = FrameNome(janela)
frame_nome1.grid()


janela.mainloop()