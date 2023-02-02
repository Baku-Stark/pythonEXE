# IMPORT [pip install rich]
from rich import print

sucess_status = "Funções ativadas com sucesso"
print(f'[on white] [black] [ON-MODE] [/black] [/on white][on cyan] [bold]{sucess_status}[/bold] [/on cyan]')

error_status = "Nenhuma função foi encontrada"
print(f'[on white] [black] [OFF-REF] [/black] [/on white][on red] [bold]{error_status}[/bold] [/on red]')