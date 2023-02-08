from tkinter import *

janela = Tk()
janela.title("Login")

Label(janela, text="Usuário: ").grid(row=0, column=0, sticky=W)
Label(janela, text="Senha: ").grid(row=1, column=0, sticky=W)

# ===============================
text_usuario = Entry(janela)
text_usuario.grid(row=0, column=1)

text_senha = Entry(janela)
text_senha.grid(row=1, column=1)

cmd_login = Button(janela, text="Login")
cmd_login.grid(row=2, column=1, sticky=E)

janela.mainloop()