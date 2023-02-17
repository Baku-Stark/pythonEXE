import os
import sys

# IMPORT [art = pip install art]
from art import *

# IMPORT [rich = pip install rich]
from rich import print as rprint


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wish.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    os.system('cls')

    try:
        tprint("Wish List", font="starwars")
        app_status = "[ON-MODE]"
        app_message = "[bold green]DJANGO[/bold green] Server successfully created!"
        rprint(f'[on white] [black] {app_status} [/black] [/on white][on blue] [bold white]{app_message}[/bold white] [/on blue]')
    
    except Exception as e:
        app_status = "[ERROR]"
        app_message = f"Some error in starting the server... {e}"
        rprint(f'[on white] [black] {app_status} [/black] [/on white][on red] [bold white]{app_message}[/bold white] [/on red]')
        
    else:
        main()