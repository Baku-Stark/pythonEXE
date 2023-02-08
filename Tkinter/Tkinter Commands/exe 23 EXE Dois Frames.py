from tkinter import *

janela = Tk()
janela.title("EXERCÍCIO COM UTILIZAÇÃO DE DUAS FRAMES")

# ----------------------------------------
# Frames
frame_nome = Frame(janela)
frame_morada = Frame(janela)

label_nome = Label(frame_nome, text="Nome: ")
label_apelido = Label(frame_nome, text="Apelido: ")
label_rua = Label(frame_morada, text="Rua: ")
label_cidade = Label(frame_morada, text="Cidade: ")

text_nome = Entry(frame_nome)
text_apelido = Entry(frame_nome)
text_rua = Entry(frame_morada)
text_cidade = Entry(frame_morada)

cmd_save = Button(janela, text="Salvar")

# ----------------------------------------
# layout
frame_nome.grid(row=0, column=0)
frame_morada.grid(row=0, column=1)

label_nome.grid(row=0, column=0)
text_nome.grid(row=0, column=1)

label_apelido.grid(row=1, column=0)
text_apelido.grid(row=1, column=1)

label_rua.grid(row=2, column=0)
text_rua.grid(row=2, column=1)

label_cidade.grid(row=3, column=0)
text_cidade.grid(row=3, column=1)

cmd_save.grid()


janela.mainloop()