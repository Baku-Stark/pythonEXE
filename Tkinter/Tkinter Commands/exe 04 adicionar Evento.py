from tkinter import *

janela = Tk()
janela.title("Adicionando Evento")
janela.geometry("500x300")

# === Evento ===
def cmd_Click():
    print('Olá, Mundo!!')

def cmda_Click():
    print('Seja bem-vindo ao Python!')


# === Janela ===
cmd = Button(janela, text="Executar", command=cmd_Click,)
cmd.pack()

cmd_a = Button(janela, text="Clicar", command=cmda_Click,)
cmd_a.pack()

janela.mainloop()
