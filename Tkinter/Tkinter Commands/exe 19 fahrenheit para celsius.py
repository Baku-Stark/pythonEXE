from tkinter import *

janela = Tk()
janela.geometry("300x120")
janela.title("FAHRENHEIT PARA CELSIUS")

# ----------------------------------------
# funções
def convert():
    fahr = float(insert_fahr.get())
    celsius = (fahr - 32) * 5/9
    text_result['text'] = f"Grau Celsius: {celsius:.1f}°C"
    text_result['font'] = 'Arial 15 bold'

# ----------------------------------------
# widgets
text_title = Label(
    janela, text="Inserir Fahrenheit:", font=('Arial 10'),
    anchor=W)

insert_fahr = Entry(janela)
text_result = Label(janela, text="- - -")

cmd_convert = Button(janela, text="Converter",command=convert)

# ----------------------------------------
# layout
text_title.pack()

insert_fahr.pack()
text_result.pack()

cmd_convert.pack()

# ----------------------------------------
# Execução
janela.mainloop()