import os
from console.utils import set_title

# IMPORT [RICH]
from rich import print as rprint

# IMPORT [functions > crud]
from functions.crud import *


class mainPainel(CRUD_APP):
    def __init__(self):
        set_title(f'Bloco De Notas | Usuário: {os.getlogin()}')
        
        while True:
            self.tableCRUD()

            self.userChoice = str(input('commando: ')).lower().strip()
            print('')
            if self.userChoice == 'read':
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
                if self.res == 'y':
                    break
                else:
                    continue

            else:
                rprint('[bold red]Comando Negado... Tente Novamente![/bold red]')

            print('')
            print('──' *50)

if __name__ == '__main__':
    os.system('cls')
    mainPainel()

    app_situation = "[Python - APP]"
    message = f"[bold green]{os.getlogin()}[/bold green] aplicação foi interrompida com sucesso!"
    rprint(f'[on white] [black] {app_situation} [/black] [/on white][on blue] [bold]{message}[/bold] [/on blue]')