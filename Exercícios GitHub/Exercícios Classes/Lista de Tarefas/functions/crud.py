import os
from rich import print as rprint
from rich.console import Console
from rich.table import Table

class CRUD_APP():
    def cleanConsole(self):
        os.system('cls')

    def tableCRUD(self):
        self.table = Table(title="COMANDOS DA APLICAÇÃO")
        
        self.table.add_column("Descrição", justify='center')
        self.table.add_column("Comando", justify='center', style="#1ADEED")

        self.table.add_row("Ler todas as anotações criadas", "read")
        self.table.add_row("Atualizar uma função", "update")
        self.table.add_row("Criar uma nova anotação", "create")
        self.table.add_row("Deletar função", "delete")
        self.table.add_row("Mostrar a lista de comandos", "help")
        self.table.add_row("Limpar o console", "cls")
        self.table.add_row("Fechar a aplicação", "end")

        console = Console()
        console.print(self.table)

    def readNoteUS(self):
        with self.con:
            app_situation = "[Leitura]"
            message = "Leitura do bloco de notas"
            rprint(f'[on white] [black] {app_situation} [/black] [/on white][on blue] [bold]{message}[/bold] [/on blue]')
            print('──' *50)
            print('')
            self.table_read = Table(title=f"Bloco de Notas de {os.getlogin()}")
            self.table_read.add_column("ID", justify='center', style="#FF241C")
            self.table_read.add_column("Anotação", justify='center')
            self.table_read.add_column("Situação", justify='center')

            # nome da tabela: tasks
            cur = self.con.cursor()
            query = 'SELECT * FROM tasks'
            cur.execute(query)
            dados = cur.fetchall()
            
            for item in dados:
                self.table_read.add_row(item[0], item[1], item[2])
            
            console = Console()
            console.print(self.table_read)
            cur.close()

    def checkNoteID(self, task_id:str, task_note, task_status):
        with self.con:
            # nome da tabela: tasks
            cur = self.con.cursor()
            query = 'SELECT id FROM tasks'
            cur.execute(query)
            dados = cur.fetchall()

            self.task_id = task_id
            self.task_id_check = ""
            self.count = 0

            for item_id in dados:
                if task_id == str(item_id[self.count]):
                    self.task_id_check = str(item_id[self.count])
                    status_title = "[INVALID - ID]"
                    status_message = "Valores iguais de ID foram encontrados!"
                    rprint(f'[on white] [black] {status_title} [/black] [/on white][on red] [bold]{status_message}[/bold] [/on red]')
                    break
            
            while self.task_id == self.task_id_check:
                    self.task_id = str(input('(REFAZENDO)Escolha um ID da sua anotação\nr: ')).strip()
                    print('')   
            
            # nome da tabela: tasks
            cur = self.con.cursor()
            query = f'INSERT INTO tasks(id, note, status) VALUES ("{self.task_id}", "{task_note}", "{task_status}")'
            cur.execute(query)
            cur.close()

            status_title = "[VALID]"
            status_message = "Nova anotação criada com sucesso!"
            rprint(f'[on white] [black] {status_title} [/black] [/on white][on blue] [bold]{status_message}[/bold] [/on blue]')

    def createNote(self):
        with self.con:
            app_situation = "[Criar Anotação]"
            message = "Criar uma nova anotação"
            rprint(f'[on white] [black] {app_situation} [/black] [/on white][on blue] [bold]{message}[/bold] [/on blue]')
            print('──' *50)
            print('')

            self.task_id = str(input('Escolha um ID da sua anotação\nr: ')).strip()
            print('')
            self.task_note = str(input('Anotação\nr: ')).strip()
            print('')
            self.task_status = "Fazendo"
            print('')
            

            if self.task_id == "" or self.task_note == "":
                status_title = "[INVALID]"
                status_message = "Os campos devem ser preenchidos... Faça novamente!"
                rprint(f'[on white] [black] {status_title} [/black] [/on white][on red] [bold]{status_message}[/bold] [/on red]')
                
                while self.task_id == "" or self.task_note == "":
                    self.task_id = str(input('(REFAZENDO)Escolha um ID da sua anotação\nr: ')).strip()
                    print('')
                    self.task_note = str(input('(REFAZENDO)Anotação\nr: ')).strip()
                    print('')
                    self.task_status = "Fazendo"
                    print('')

                    # nome da tabela: tasks
                    cur = self.con.cursor()
                    query = f'INSERT INTO tasks(id, note, status) VALUES ("{self.task_id}", "{self.task_note}", "{self.task_status}")'
                    cur.execute(query)
                    cur.close()

                    status_title = "[VALID]"
                    status_message = "Nova anotação criada com sucesso!"
                    rprint(f'[on white] [black] {status_title} [/black] [/on white][on blue] [bold]{status_message}[/bold] [/on blue]')

            else:
                self.checkNoteID(self.task_id, self.task_note, self.task_status)

    def updateNote(self):
        self.readNoteUS()
        app_situation = "[Apagar Anotação]"
        message = "Atualizar anotação desejada"
        rprint(f'[on white] [black] {app_situation} [/black] [/on white][on red] [bold]{message}[/bold] [/on red]')

        with self.con:
            self.task_id = str(input('Escolha o ID para atualizar a anotação\nr: ')).strip()
            print('')
            self.task_status = str(input('Cite o novo status da anotação\nr: ')).strip()
            print('')

            if self.task_id == "" or self.task_status == "":
                while self.task_id == "" or self.task_status == "":
                    self.task_id = str(input('(REFAZENDO)Escolha um ID da sua anotação\nr: ')).strip()
                    print('')
                    self.task_status = str(input('(REFAZENDO)Cite o novo status da anotação\nr: ')).strip()
                    print('')
            
            # nome da tabela: tasks
            cur = self.con.cursor()
            query = f'UPDATE tasks SET status="{self.task_status}" WHERE id="{self.task_id}"'
            cur.execute(query)
            cur.close()

            status_title = "[VALID]"
            status_message = "Anotação apagada com sucesso!"
            rprint(f'[on white] [black] {status_title} [/black] [/on white][on blue] [bold]{status_message}[/bold] [/on blue]')
    
    def deleteNote(self):
        self.readNoteUS()
        app_situation = "[Apagar Anotação]"
        message = "Apagar anotação desejada"
        rprint(f'[on white] [black] {app_situation} [/black] [/on white][on red] [bold]{message}[/bold] [/on red]')

        with self.con:
            self.task_id = str(input('Escolha o ID para apagar a anotação\nr: ')).strip()

            if self.task_id == "":
                while self.task_id == "":
                    self.task_id = str(input('(REFAZENDO)Escolha um ID da sua anotação\nr: ')).strip()
                    print('')
            
            # nome da tabela: tasks
            cur = self.con.cursor()
            query = f'DELETE FROM tasks WHERE id="{self.task_id}"'
            cur.execute(query)
            cur.close()
            print('')
            status_title = "[VALID]"
            status_message = "Anotação apagada com sucesso!"
            rprint(f'[on white] [black] {status_title} [/black] [/on white][on blue] [bold]{status_message}[/bold] [/on blue]')