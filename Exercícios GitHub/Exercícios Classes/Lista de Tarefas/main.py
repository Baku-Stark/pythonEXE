import os
from console.utils import set_title

# IMPORT [RICH]
from rich import print as rprint

# IMPORT [functions > crud]
from functions.crud import *

# import[sqlite]
import sqlite3 as lite


class mainPainel(CRUD_APP):
    def __init__(self):
        set_title(f'Bloco De Notas | Usuário: {os.getlogin()}')
        try:
            self.con = lite.connect(r'db/database.db')
            self.cur = self.con.cursor()
            self.cur.execute("CREATE TABLE IF NOT EXISTS tasks(id TEXT, note TEXT, status TEXT)")

            app_situation = "[VALID]"
            message = "Lista de Tarefas criada com sucesso!"
            rprint(f'[on white] [black] {app_situation} [/black] [/on white][on green] [bold]{message}[/bold] [/on green]')
        
        except Exception as e:
            app_situation = "[INVALID]"
            message = f"A Lista de Tarefas não pode ser criada...{e}"
            rprint(f'[on white] [black] {app_situation} [/black] [/on white][on red] [bold]{message}[/bold] [/on red]')

        self.res = "y"

        while self.res == "y":
            self.userChoice = str(input('commando: ')).lower().strip()
            print('')

            if self.userChoice == 'help':
                self.tableCRUD()

            elif self.userChoice == 'read':
                self.readNoteUS()
            
            elif self.userChoice == 'create':
                self.createNote()

            elif self.userChoice == 'update':
                self.updateNote()

            elif self.userChoice == 'delete':
                self.deleteNote()

            elif self.userChoice == 'cls':
                self.cleanConsole()

            elif self.userChoice == 'end':
                rprint('[red]Deseja interromper a aplicação?[/red]')
                self.res = str(input('[y/n]: ')).lower().strip()

            else:
                rprint('[bold red]Esse comando não existe... Tente Novamente![/bold red]')

            print('')
            print('──' *50)

if __name__ == '__main__':
    os.system('cls')
    mainPainel()

    app_situation = "[Python - APP]"
    message = f"[bold green]{os.getlogin()}[/bold green] aplicação foi interrompida com sucesso!"
    rprint(f'[on white] [black] {app_situation} [/black] [/on white][on blue] [bold]{message}[/bold] [/on blue]')