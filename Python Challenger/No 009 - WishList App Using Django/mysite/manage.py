# =====================================================================
# IMPORT [art(ascii) > pip install art]
from art import *

# IMPORT [pip install rich]
from rich import print as rprint

# IMPORT [SQLITE]
import sqlite3 as lite
from Wish.db_functions import readWish

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

    try:
        con = lite.connect('wish-database.db')
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS wish_list(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                wish_title TEXT,
                my_wish TEXT
            )
        """)

        sucess_db = "[bold]DATABASE[/bold] successfully created!!"
        rprint(f'[on white] [black] [ON-MODE] [/black] [/on white][on blue] [bold]{sucess_db}[/bold] [/on blue]')

        readWish()

        sucess_status = "[bold green]DJANGO[/bold green] server successfully created!"
        rprint(f'[on white] [black] [ON-MODE] [/black] [/on white][on blue] [bold]{sucess_status}[/bold] [/on blue]')
        server_name = "WELCOME"
        tprint(server_name, font="starwars")

    except Exception as e:
        error_db = "Something went wrong..."
        rprint(f'[on white] [black] [OFF-REF] [/black] [/on white][on red] [bold]{error_db}[/bold] [/on red]')
        rprint(f'[on red]{e}[/on red]')

    main()

else:
    error_status = "No function found"
    rprint(f'[on white] [black] [OFF-REF] [/black] [/on white][on red] [bold]{error_status}[/bold] [/on red]')
