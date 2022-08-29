from tkinter import *

janela = Tk()
janela.geometry("300x150")
janela.title("FRAME E INSTANCIAÇÃO")

# ----------------------------------------
# função
class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()

        self['bd'] = "1"
        self['relief'] = SOLID

        self.label1_text = StringVar()
        self.text1_text = StringVar()

        self.label1 = Label(self, textvariable=self.label1_text)
        text1 = Entry(self, textvariable=self.text1_text)
        cmd1 = Button(self, text="Clique", command=self.Executar)

        self.label1.grid()
        text1.grid()
        cmd1.grid()

    def Executar(self):
        self.label1_text.set('Olá, ' + self.text1_text.get() + '.')

# ----------------------------------------
# Frame
frm1 = MinhaFrame(janela)
frm1.grid()

frm2 = MinhaFrame(janela)
frm2.grid()

janela.mainloop()