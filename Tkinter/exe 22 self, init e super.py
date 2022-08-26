from tkinter import *

janela = Tk()
janela.title("SELF, INIT E SUPER")

# ----------------------------------------
# widget
class MinhaFrame(Frame):
    def __init__(self, janela):
        super().__init__()
        self['bg'] = 'blue'
        self['width'] = 400
        self['height'] = 200

# ----
frame = MinhaFrame(janela)
frame.grid()


janela.mainloop()