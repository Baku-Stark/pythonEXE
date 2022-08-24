from tkinter import *

janela = Tk()
janela.title("Tabuada")
janela.geometry("500x250")
janela.resizable(width=FALSE, height=FALSE)


# ----------------------------------------
# cores
cor_bg = "#111111"
cor_wr = "#dcf1f2"

# ----------------------------------------
# função
def multi():
    num = int(select.get())
    painel['text'] = " "
    for n in range(1, 11):
        print(f"{num} x {n} = {num*n}")

        resultado = Label(
            janela, text=f"{num} x {n} = {num*n}", font=('Arial 14 bold'),
            bg=cor_bg, fg=cor_wr, justify=LEFT, anchor=W
        )

        resultado.pack()

# ----------------------------------------
# widget
text_title = Label(
    janela, text="Escolha um número: ",
    font=('Arial 10 bold')
)

select = Entry(janela)

cmd_multi = Button(
    janela, text="Multiplicar", command=multi
)

painel = Label(
    janela, text="---", font=('Arial 15 bold'),
    bg=cor_bg, fg=cor_wr, width=30, height=17,
    justify=LEFT, anchor=NW
)

# ----------------------------------------
# layout
text_title.place(x=0, y=0)
select.place(x=0, y=40)
cmd_multi.place(x=0, y=60)

painel.place(x=200, y=0)

# ----------------------------------------
# execução
janela.mainloop()