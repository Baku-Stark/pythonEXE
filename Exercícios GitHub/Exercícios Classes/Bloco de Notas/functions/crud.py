import os
from rich import print as rprint
from rich.console import Console
from rich.table import Table

class CRUD_APP():
    '''
        'r'  -> Usado somente para ler algo;
        'r+' -> Usado para LER e ESCREVER algo;
        'w'  -> Usado somente para escrever algo;
        'w+' -> escrita (o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo);
        'a'  -> Usado para acrescentar algo;
        'a+' -> leitura e escrita (abre o arquivo para atualização)
    '''

    def tableCRUD(self):
        self.table = Table(title="COMANDOS DA APLICAÇÃO")
        
        self.table.add_column("Descrição", justify='center')
        self.table.add_column("Comando", justify='center', style="#1ADEED")

        self.table.add_row("Ler todas as anotações criadas", "read")
        self.table.add_row("Atualizar uma função", "update")
        self.table.add_row("Criar uma nova anotação", "create")
        self.table.add_row("Deletar função", "delete")
        self.table.add_row("Limpar o console", "cls")
        self.table.add_row("Fechar a aplicação", "end")

        console = Console()
        console.print(self.table)

    def cleanConsole(self):
        os.system('cls')

    def readNoteUS(self):
        app_situation = "[Leitura]"
        message = "Leitura do bloco de notas"
        rprint(f'[on white] [black] {app_situation} [/black] [/on white][on blue] [bold]{message}[/bold] [/on blue]')
        print('──' *50)
        print('')
        self.table_read = Table(title=f"Bloco de Notas de {os.getlogin()}")
        
        self.table_read.add_column("ID", justify='center', style="#FF241C")
        self.table_read.add_column("Anotação", justify='center')
        self.table_read.add_column("Situação", justify='center')

        with open(r'db/notes.txt', 'r') as note_file:
            for linha in note_file:
                dado = linha.split(';')
                self.table_read.add_row(str(dado[0]), dado[1], dado[2])
        
        console = Console()
        console.print(self.table_read)

    def createNote(self):
        app_situation = "[Criar Anotação]"
        message = "Digite a anotação que você deseja fazer"
        rprint(f'[on white] [black] {app_situation} [/black] [/on white][on green] [bold]{message}[/bold] [/on green]')
        print('')
        print('──' *50)

        self.created_task = 'False'
        self.success_task = 'False'

        while self.created_task == 'False':

            rprint('[green]-> Escolha um ID[/green]')
            self.task_id = str(input('r: '))
            if len(self.task_id) > 9:
                rprint("[bold red](ERRO) - O 'ID' aceita 9 caracteres no total[/bold red]")
                while len(self.task_id) > 9:
                    self.task_id = str(input('-> (REFAZENDO\nr: '))
            
            print('')

            rprint('[green]-> Escreva a anotação[/green]')
            self.task_user = str(input('note: '))
            if  len(self.task_user) > 40:
                rprint("[bold red](ERRO) - A 'ANOTAÇÃO' aceita 40 caracteres no total[/bold red]")
                while len(self.task_user) > 40:
                    self.task_user = str(input('(REFAZENDO) note: '))
            
            with open(r'db/notes.txt', 'r') as note_file:
                for linha in note_file:
                    dado = linha.split(';')
                    if self.task_id == str(dado[0]):
                        self.success_task = 'False'

                    else:
                        self.success_task = 'True'

            if self.success_task == 'True':
                self.created_task = 'True'

                with open(r'db/notes.txt', 'a+') as note_fileUP:
                    note_fileUP.write(f'{self.task_id};{self.task_user};Para Fazer\n')

                function_status = "[VALID]"
                func_message = "Anotação criada!!!"
                rprint(f'[on white] [black] {function_status} [/black] [/on white][on green] [bold]{func_message}[/bold] [/on green]')
            
            else:
                self.created_task = 'False'
                function_status = "[INVALID]"
                func_message = "O ID que voce escolheu está inválido... Faça novamente!!!"
                rprint(f'[on white] [black] {function_status} [/black] [/on white][on red] [bold]{func_message}[/bold] [/on red]')
                print('')

    def updateNote(self):
        app_situation = "[Atualizar Anotação]"
        message = "Selecione o ID da anotação para atualizar"
        rprint(f'[on white] [black] {app_situation} [/black] [/on white][on green] [bold]{message}[/bold] [/on green]')
        print('──' *50)
        print('')
    
    def deleteNote(self):
        app_situation = "[Apagar Anotação]"
        message = f"Selecione o ID da anotação para apagar"
        rprint(f'[on white] [black] {app_situation} [/black] [/on white][on red] [bold]{message}[/bold] [/on red]')
        print('──' *50)
        print('')

        self.table_read = Table(title=f"Bloco de Notas de {os.getlogin()}")
        
        self.table_read.add_column("ID", justify='center', style="#FF241C")
        self.table_read.add_column("Anotação", justify='center')
        self.table_read.add_column("Situação", justify='center')

        self.task_id = str(input('Insira o ID da anotação\nID: '))
        print('')
        with open(r'db/notes.txt', 'r') as note_file:
            for linha in note_file:
                dado = linha.split(';')
                if self.task_id == dado[0]:
                    self.table_read.add_row(str(dado[0]), dado[1], dado[2])

        console = Console()
        console.print(self.table_read)