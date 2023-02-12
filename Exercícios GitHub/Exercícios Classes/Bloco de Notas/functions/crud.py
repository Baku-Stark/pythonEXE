import os
from rich import print as rprint
from rich.console import Console
from rich.table import Table

class CRUD_APP():
    def tableCRUD(self):
        self.table = Table(title=f"BEM-VINDO !!!")
        
        self.table.add_column("Descrição", justify='center')
        self.table.add_column("Comando", justify='center', style="#1ADEED")

        self.table.add_row("Limpar o console", "cls")
        self.table.add_row("Fechar a aplicação", "end")
        self.table.add_row("Deletar função", "delete-note")
        self.table.add_row("Atualizar uma função", "update-note")
        self.table.add_row("Criar uma nova anotação", "create-note")
        self.table.add_row("Ler todas as anotações criadas", "read-note")

        console = Console()
        console.print(self.table)

    def cleanConsole(self):
        os.system('cls')

    def readNoteUS(self):
        app_situation = "[Leitura]"
        message = "Leitura do bloco de notas"
        rprint(f'[on white] [black] {app_situation} [/black] [/on white][on blue] [bold]{message}[/bold] [/on blue]')
        self.table_read = Table(title=f"Bloco de Notas de {os.getlogin()}")
        
        self.table_read.add_column("ID", justify='center', style="#1ADEED")
        self.table_read.add_column("Anotação", justify='center')
        self.table_read.add_column("Situação", justify='center')

        self.table_read.add_row("219180312", "Limpar casa do cachorro", "Para Fazer")
        console = Console()
        console.print(self.table_read)

    def createNote(self):
        app_situation = "[Criar Anotação]"
        message = "Digite a anotação que você deseja fazer"
        rprint(f'[on white] [black] {app_situation} [/black] [/on white][on green] [bold]{message}[/bold] [/on green]')

    def updateNote(self):
        app_situation = "[Atualizar Anotação]"
        message = "Selecione o ID da anotação para atualizar"
        rprint(f'[on white] [black] {app_situation} [/black] [/on white][on green] [bold]{message}[/bold] [/on green]')
    
    def deleteNote(self):
        app_situation = "[Apagar Anotação]"
        message = f"Selecione o ID da anotação para apagar"
        rprint(f'[on white] [black] {app_situation} [/black] [/on white][on red] [bold]{message}[/bold] [/on red]')