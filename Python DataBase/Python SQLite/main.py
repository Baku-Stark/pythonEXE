import os, platform
sys_op = platform.system()

import sqlite3 as lite
from services.__COLORS import Colors
from services.__TempPrint import TempPrint

if not os.path.exists("db/database.db"):
    os.mkdir("db")

    print(Colors.BACK_YELLOW + " Python " + Colors.END, end='')
    print(Colors.YELLOW + " Created folder n' file (/db/database.db)" + Colors.END)

con = lite.connect('db/database.db')

from services.__REGEX import regex_email

class App():
    def __init__(self):
        self.start()

        if sys_op == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

        # self.create()
        self.read()
        self.update()
        self.delete()

    def start(self):
        """
            Start and create a Database
        """

        # ----------------------------------------
        # Tabela
        try:
            TempPrint(message="[-] Creating your table...").TPrint()

            with con:
                cur = con.cursor()

                cur.execute(
                    """
                        CREATE TABLE IF NOT EXISTS form(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT,
                            email TEXT,
                            created_at Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                            updated_at Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                        )
                    """
                )

            print(Colors.BACK_GREEN + " SQLite3 " + Colors.END, end='')
            print(Colors.GREEN + " Table Started! " + Colors.END)
        
        except Exception as error:
            print(Colors.BACK_RED + " SQLite3 " + Colors.END, end='')
            print(Colors.RED + f" {error} " + Colors.END)

    def create(self):
        nome = str(input("What's your name?\nr: "))
        print('')
        email = str(input("Type your email\nr: "))
        print('')

        if regex_email(email):
            try:
                with con:
                    cur = con.cursor()
                    query = "INSERT INTO form (nome, email) VALUES (?, ?)"
                    i = [nome, email]
                    cur.execute(query, i)

                TempPrint(message="[-] Creating new item...").TPrint()
                print(Colors.BACK_GREEN + " SQLite3 " + Colors.END, end='')
                print(Colors.GREEN + " Created! " + Colors.END)
            
            except Exception as error:
                print(Colors.BACK_RED + " SQLite3 " + Colors.END, end='')
                print(Colors.RED + f" {error} " + Colors.END)

    def read(self):
        with con:
            cur = con.cursor()
            query = "SELECT * FROM form"
            cur.execute(query)
            info = cur.fetchall()

            for item in info:
                print(item)

    def update(self):
        item_id = int(input("Type item id: "))
        print('')

        new_name = str(input("[Update] Name\nr: "))
        print('')
        new_email = str(input("[Update] Email\nr: "))
        print('')

        try:
            with con:
                cur = con.cursor()
                query = f"UPDATE form SET nome='{new_name}', email='{new_email}' WHERE id={item_id}"
                cur.execute(query)

                TempPrint(message="[-] Updating your item...").TPrint()
                print(Colors.BACK_GREEN + " SQLite3 " + Colors.END, end='')
                print(Colors.GREEN + " Updated! " + Colors.END)

        except Exception as error:
                print(Colors.BACK_RED + " SQLite3 " + Colors.END, end='')
                print(Colors.RED + f" {error} " + Colors.END)
    
    def delete(self):
        item_id = int(input("Type item id: "))
        print('')

        try:
            with con:
                cur = con.cursor()
                query = f"DELETE FROM form WHERE id={item_id}"
                cur.execute(query)

                TempPrint(message="[-] Deleting your item...").TPrint()
                print(Colors.BACK_GREEN + " SQLite3 " + Colors.END, end='')
                print(Colors.GREEN + " Deleted! " + Colors.END)

        except Exception as error:
                print(Colors.BACK_RED + " SQLite3 " + Colors.END, end='')
                print(Colors.RED + f" {error} " + Colors.END)

if __name__ == '__main__':
    App()
    con.close()