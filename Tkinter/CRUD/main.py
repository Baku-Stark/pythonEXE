from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# importação do calendário
from tkcalendar import Calendar, DateEntry

# importação do VIEW e DATABASE
from view import *

# ----------------------------------------
# Janela
root = Tk()
root.title("")
root.geometry("1043x453")
root.configure(background="#f0f8ff")
root.resizable(width=FALSE, height=FALSE)

# ----------------------------------------
# Cores
cor_bg = "#141726"
cor_bg2 = "#fcfcfc"
cor_text = "#f0f8ff"
cor_text2 = "#111111"

# ----------------------------------------
# Função
global tree

def show():
    global tree
    lista = acess()

    tabela_head = ['ID', 'Nome',  'Email', 'Telefone', 'Data', 'Estado', 'Sobre']

    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    tree = ttk.Treeview(
    frame_left, selectmode="extended", columns=tabela_head, show="headings"
    )

    vsb = ttk.Scrollbar(
        frame_left, orient="vertical", command=tree.yview
    )

    hsb = ttk.Scrollbar(
        frame_left, orient="horizontal", command=tree.xview
    )

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    frame_left.grid_rowconfigure(0, weight=12)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)


def insert_info():
    nome = e_nome.get()
    email = e_email.get()
    tel = e_telefone.get()
    data = e_date.get()
    estado = e_situation.get()
    info = e_info.get()

    lista = [nome, email, tel, data, estado, info]

    if nome == "":
        messagebox.showwarning("Erro!", "O usuário precisa registrar um nome!")

    else:
        insert(lista)
        messagebox.showinfo("Inserção conluída", "O cadastro foi realizado com sucesso!")

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_date.delete(0, 'end')
        e_situation.delete(0, 'end')
        e_info.delete(0, 'end')
    
    for widget in frame_left.winfo_children():
        widget.destroy()

    show()


def update_info():
    try:
        treev_dados = tree.focus()
        treev_dic = tree.item(treev_dados)
        tree_list = treev_dic['values']

        valor_id = tree_list[0]

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_date.delete(0, 'end')
        e_situation.delete(0, 'end')
        e_info.delete(0, 'end')

        e_nome.insert(0, tree_list[1])
        e_email.insert(0, tree_list[2])
        e_telefone.insert(0, tree_list[3])
        e_date.insert(0, tree_list[4])
        e_situation.insert(0, tree_list[5])
        e_info.insert(0, tree_list[6])
        
        # --- REwrite
        def updateCheck():
            nome = e_nome.get()
            email = e_email.get()
            tel = e_telefone.get()
            data = e_date.get()
            estado = e_situation.get()
            info = e_info.get()

            lista = [nome, email, tel, data, estado, info, valor_id]

            if nome == "":
                messagebox.showwarning("Erro!", "O usuário precisa registrar um nome!")

            else:
                update(lista)
                messagebox.showinfo("Inserção conluída", "Os dados foram atualizados com sucesso!")

                e_nome.delete(0, 'end')
                e_email.delete(0, 'end')
                e_telefone.delete(0, 'end')
                e_date.delete(0, 'end')
                e_situation.delete(0, 'end')
                e_info.delete(0, 'end')
            
            for widget in frame_left.winfo_children():
                widget.destroy()
            
            show()

        btn_confirmar = Button(
            frame_baixo, text="Confirmar",
            font=('Arial 10 bold'), fg=cor_text,
            bg="#03588C", relief='raised',
            overrelief='ridge', command=updateCheck)

        btn_confirmar.place(x=95, y=370)

    except IndexError:
        messagebox.showerror("Erro", "Selecione um dos dados na tabela!")


def delete_info():
    try:
        treev_dados = tree.focus()
        treev_dic = tree.item(treev_dados)
        tree_list = treev_dic['values']

        valor_id = [tree_list[0]]

        delete(valor_id)
        messagebox.showinfo("Sucesso!", "Os dados foram deletados da lista de consulta!")

        for widget in frame_left.winfo_children():
                widget.destroy()
            
        show()

    except IndexError:
        messagebox.showerror("Erro", "Selecione um dos dados na tabela!")

# ----------------------------------------
# Frames
class FrameCima(Frame):
    def __init__(self, root):
        super().__init__()
        self['bg'] = cor_bg
        self['width'] = 310
        self['height'] = 50
        self['relief'] = 'flat'

class FrameBaixo(Frame):
    def __init__(self, root):
        super().__init__()
        self['bg'] = cor_bg2
        self['width'] = 310
        self['height'] = 403
        self['relief'] = 'flat'

class FrameLeft(Frame):
    def __init__(self, root):
        super().__init__()
        self['bg'] = cor_bg2
        self['width'] = 588
        self['height'] = 403
        self['relief'] = 'flat'

# ----------------------------------------
# Widgets
frame_cima = FrameCima(root)
# ----------------------------------------
app_nome = Label(
    frame_cima, text="Formulário de Consultoria",
    font=('Ivy 13 bold'), bg=cor_bg, fg=cor_text, anchor=NW
)

# ----------------------------------------
frame_baixo = FrameBaixo(root)
# ----------------------------------------
# --- Nome
l_nome = Label(
    frame_baixo, text="Nome *",
    font=('Ivy 10 bold'), bg=cor_bg2, fg=cor_text2, anchor=NW
)
e_nome = Entry(
    frame_baixo, fg=cor_text2, width=45, justify=LEFT,
    relief='solid'
)

# --- Email
l_email = Label(
    frame_baixo, text="E-mail *",
    font=('Ivy 10 bold'), bg=cor_bg2, fg=cor_text2, anchor=NW
)
e_email = Entry(
    frame_baixo, fg=cor_text2, width=45, justify=LEFT,
    relief='solid'
)

# --- Telefone
l_telefone = Label(
    frame_baixo, text="Telefone *",
    font=('Ivy 10 bold'), bg=cor_bg2, fg=cor_text2, anchor=NW
)
e_telefone = Entry(
    frame_baixo, fg=cor_text2, width=45, justify=LEFT,
    relief='solid'
)

# --- Data da consulta
l_date = Label(
    frame_baixo, text="Data Da Consulta *",
    font=('Ivy 10 bold'), bg=cor_bg2, fg=cor_text2, anchor=NW
)
e_date = DateEntry(
    frame_baixo, year=2022, fg=cor_text2, width=12, justify=LEFT,
    relief='solid'
)

# --- Estado da consulta
l_situation = Label(
    frame_baixo, text="Estado Da Consulta *",
    font=('Ivy 10 bold'), bg=cor_bg2, fg=cor_text2, anchor=NW
)
e_situation = Entry(
    frame_baixo, fg=cor_text2, width=20, justify=LEFT,
    relief='solid'
)

# --- Informação extra
l_info = Label(
    frame_baixo, text="Informação Da Consulta*",
    font=('Ivy 10 bold'), bg=cor_bg2, fg=cor_text2, anchor=NW
)
e_info = Entry(
    frame_baixo, fg=cor_text2, width=45, justify=LEFT,
    relief='solid'
)

# --- Botões
btn_insert = Button(
    frame_baixo, text="Inserir", font=('Arial 12 bold'),
    fg=cor_text, bg="#0477BF", relief='raised', overrelief='ridge', command=insert_info
)

btn_update = Button(
    frame_baixo, text="Atualizar", 
    font=('Arial 12 bold'), fg=cor_text, bg="#03588C",
    relief='raised', overrelief='ridge', command=update_info
)

btn_delete = Button(
    frame_baixo, text="Deletar", font=('Arial 12 bold'),
    fg=cor_text, bg="#012E40", relief='raised', overrelief='ridge', command=delete_info
)

# ----------------------------------------
frame_left = FrameLeft(root)
# ----------------------------------------

# ----------------------------------------
# Painel
frame_cima.grid(row=0, column=0)
app_nome.place(x=10, y=20)

frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)
l_nome.place(x=10, y=10)
e_nome.place(x=15, y=40)
# ---
l_email.place(x=10, y=70)
e_email.place(x=15, y=100)
# ---
l_telefone.place(x=10, y=130)
e_telefone.place(x=15, y=160)
# ---
l_date.place(x=15, y=190)
e_date.place(x=15, y=220)
# ---
l_situation.place(x=155, y=190)
e_situation.place(x=157, y=220)
# ---
l_info.place(x=15, y=260)
e_info.place(x=15, y=290)
# ---
btn_insert.place(x=15, y=330)
btn_update.place(x=95, y=330)
btn_delete.place(x=195, y=330)

frame_left.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)


show()
root.mainloop()