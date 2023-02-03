# =====================================================================
# IMPORT [pip install rich]
from rich import print

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
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
    sucess_status = "Servidor [bold green]DJANGO[/bold green] criado com sucesso!"
    print(f'[on white] [black] [ON-MODE] [/black] [/on white][on blue] [bold]{sucess_status}[/bold] [/on blue]')
    main()

else:
    error_status = "Nenhuma função foi encontrada"
    print(f'[on white] [black] [OFF-REF] [/black] [/on white][on red] [bold]{error_status}[/bold] [/on red]')
