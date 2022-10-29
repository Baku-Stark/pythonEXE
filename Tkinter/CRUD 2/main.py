# ===============================================
# IMPORTAÇÕES
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from functions import *

# ===============================================
# CORES
bg_root = "#111111"
fg_root = "#111111"

bg_button = "#111111"
fg_button = "#f0f8ff"

frame_top_bottom = "#f0f8ff"
hl_bg = "#9C9FA6"

# ===============================================
# FUNÇOES
class Funcs():
    # Ler banco de dados [database.db]
    def readTable(self):
        lista = readCRUD()

        for item in lista:
            self.listaCli.insert('', 'end', values=item)
    
    # Limpar Conteúdo [st_Limpar]
    def limpar_tela(self):
        self.codigo_entry.delete(0, 'end')
        self.nome_entry.delete(0, 'end')
        self.telefone_entry.delete(0, 'end')
        self.cidade_entry.delete(0, 'end')

    # Inserir Usuário [st_Novo]
    def novo_usuario(self):
        codigoUser = self.codigo_entry.get()
        nomeUser = self.nome_entry.get()
        telefoneUser = self.telefone_entry.get()
        cidadeUser = self.cidade_entry.get()

        # ---- [CÓDIGO]
        if codigoUser == "" and nomeUser == "":
            messagebox.showwarning(
                title="Código e/ou Nome",
                message="CÓDIGO e NOME são obrigados para o registro."
            )

        elif codigoUser == "":
            messagebox.showwarning(
                title="Inserção de código vazia",
                message="O usuário precisa preencher a opção CÓDIGO para fazer um novo cadastro."
            )
        # ---- [CÓDIGO]

        # ---- [NOME]
        elif nomeUser == "":
            messagebox.showwarning(
                title="Inserção de nome vazia",
                message="O usuário precisa preencher a opção Nome para fazer um novo cadastro."
            )
        # ---- [NOME]

        # ---- [TELEFONE]
        elif len(telefoneUser) > 9:
            messagebox.showwarning(
                title="Inserção de telefone inválida",
                message="O número de telefone ultrapassou o limite de dígitos."
            )
            self.telefone_entry.delete(0, 'end')

        elif len(telefoneUser) < 8:
            messagebox.showwarning(
                title="Inserção de telefone inválida",
                message="O telefone precisa (no máximo) de 8 dígitos para a autocorreção funcionar."
            )
            self.telefone_entry.delete(0, 'end')

        elif len(telefoneUser) == 8:
            messagebox.showwarning(
                title="Correção no número de telefone",
                message="O número de telefone possui 8 dígitos. Então, o programa adicionou um '9' na frente."
            )

            telefoneUser = f"9{telefoneUser}"

            lista = [codigoUser, nomeUser, telefoneUser, cidadeUser]
            createCRUD(lista)

            messagebox.showinfo(
                title="Sucesso!",
                message="Um novo cadastro foi efetuado com sucesso!"
            )

            self.limpar_tela()
        # ---- [TELEFONE]
        
        # ---- [CIDADE]
        elif cidadeUser == "":
            cidadeUser = "Cidade não informada"

            lista = [codigoUser, nomeUser, telefoneUser, cidadeUser]
            createCRUD(lista)

            messagebox.showinfo(
                title="Sucesso!",
                message="Um novo cadastro foi efetuado com sucesso!"
            )

            self.limpar_tela()
        # ---- [CIDADE]

        # ---- [EFETUADO COM SUCESSO (sem interrupções)]
        else:
            lista = [codigoUser, nomeUser, telefoneUser, cidadeUser]
            createCRUD(lista)

            messagebox.showinfo(
                title="Sucesso!",
                message="Um novo cadastro foi efetuado com sucesso!"
            )

            self.limpar_tela()
        # ---- [EFETUADO COM SUCESSO (sem interrupções)]
    
    # Atualizar Usuário [st_Alterar]
    def atualizar_usuario(self):
        pass

    # Deletar Usuário [st_Apagar]
    def deletar_usuario(self):
        pass
# ===============================================
# JANELA [config.]
root = Tk()

class App(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_tela()
        self.frameTop_Gadgets()
        self.frameBottom_Gadgets()
        
        # --- [Funcs]
        self.readTable()
        # =======================================
        # ROOT [mainloop]
        root.mainloop()
    
    def tela(self):
        self.root.title("Python - Cadastro de Cliente")
        self.root.iconbitmap("_img/natural.ico")
        self.root.geometry("700x500")
        self.root.configure(background=bg_root)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)
        self.root.resizable(width='true', height='true')
        
    # ===========================================
    # FRAMES [top - bottom]
    def frame_tela(self):
        self.frameTop = Frame(
            self.root, bg=frame_top_bottom, bd=4,
            highlightbackground=hl_bg, highlightthickness=3
        )

        self.frameBottom = Frame(
            self.root, bg=frame_top_bottom, bd=4,
            highlightbackground=hl_bg, highlightthickness=3
        )

        # =======================================
        # INSERÇÃO DE FRAME
        self.frameTop.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        
        self.frameBottom.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    
    # ===========================================
    # Gadgets [Top_Frame]
    def frameTop_Gadgets(self):
        # -------- BUTTONS --------
        self.st_Limpar = Button(
            self.frameTop, text="Limpar",
            font=('Arial 8 bold'), bg=bg_button, fg=fg_button,
            overrelief="ridge", relief='raised'
        )
        self.st_Limpar['command'] = self.limpar_tela

        self.st_Buscar = Button(
            self.frameTop, text="Buscar",
            font=('Arial 8 bold'), bg=bg_button, fg=fg_button,
            overrelief="ridge", relief='raised'
        )

        self.st_Novo = Button(
            self.frameTop, text="Novo",
            font=('Arial 8 bold'), bg=bg_button, fg=fg_button,
            overrelief="ridge", relief='raised'
        )
        self.st_Novo['command'] = self.novo_usuario

        self.st_Alterar = Button(
            self.frameTop, text="Alterar",
            font=('Arial 8 bold'), bg=bg_button, fg=fg_button,
            overrelief="ridge", relief='raised'
        )
        self.st_Alterar['command'] = self.atualizar_usuario

        self.st_Apagar = Button(
            self.frameTop, text="Apagar",
            font=('Arial 8 bold'), bg=bg_button, fg=fg_button,
            overrelief="ridge", relief='raised'
        )
        self.st_Apagar['command'] = self.deletar_usuario
        # -------- BUTTONS --------

        # -------- LABELS N' INPUTS --------
        self.codigo = Label(
            self.frameTop, text="Código",
            font=('Arial 10 bold'), bg=frame_top_bottom
        )
        self.codigo_entry = Entry(self.frameTop)

        # ----- NOME
        self.nome = Label(
            self.frameTop, text="Nome",
            font=('Arial 10 bold'), bg=frame_top_bottom
        )
        self.nome_entry = Entry(self.frameTop)
        # ----- NOME

        # ----- TELEFONE
        self.telefone = Label(
            self.frameTop, text="Telefone",
            font=('Arial 10 bold'), bg=frame_top_bottom
        )
        self.telefone_entry = Entry(self.frameTop)
        # ----- TELEFONE

        # ----- CIDADE
        self.cidade = Label(
            self.frameTop, text="Cidade",
            font=('Arial 10 bold'), bg=frame_top_bottom
        )
        self.cidade_entry = Entry(self.frameTop)
        # ----- CIDADE
        # -------- LABELS N' INPUTS --------

        # =======================================
        # INSERÇÃO DOS GADGETS
        # -------- BUTTONS --------
        self.st_Limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        self.st_Buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.st_Novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.st_Alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        self.st_Apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        # -------- BUTTONS --------

        # -------- LABELS N' INPUTS --------
        self.codigo.place(relx=0.05, rely=0.02)
        self.codigo_entry.place(relx=0.05, rely=0.12, relwidth=0.1, relheight=0.13)

        self.nome.place(relx=0.05, rely=0.40)
        self.nome_entry.place(relx=0.05, rely=0.52, relwidth=0.80, relheight=0.13)

        self.telefone.place(relx=0.05, rely=0.7)
        self.telefone_entry.place(relx=0.05, rely=0.8, relwidth=0.30)

        self.cidade.place(relx=0.45, rely=0.7)
        self.cidade_entry.place(relx=0.45, rely=0.8, relwidth=0.30)
        # -------- LABELS N' INPUTS --------
    
    # ===========================================
    # Gadgets [Bottom_Frame]
    def frameBottom_Gadgets(self):
        colunas = ("ID", "Código", "Nome", "Telefone", "Cidade")
        self.listaCli = ttk.Treeview(
            self.frameBottom, height=3, columns=colunas, show='headings'
        )

        self.scrollY = ttk.Scrollbar(
            self.frameBottom, orient='vertical'
        )
        self.scrollY['command'] = self.listaCli.yview
        self.listaCli.configure(yscrollcommand=self.scrollY)

        listaWidth = [1, 50, 200, 125, 125]
        c = 0
        
        for col in colunas:
            self.listaCli.heading(c, text=col)
            self.listaCli.column(c, width=listaWidth[c])
            c += 1
    
        # =======================================
        # INSERÇÃO DA LISTA
        self.listaCli.place(relx=0.01, rely=0.01, relwidth=0.96, relheight=0.98)
        self.scrollY.place(relx=0.97, rely=0.01, relwidth=0.03, relheight=0.98)

# ===============================================
# EXECUÇÃO DA JANELA
if __name__ == '__main__':
    App()
    