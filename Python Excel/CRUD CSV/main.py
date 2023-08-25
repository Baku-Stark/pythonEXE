import os
import time
from datetime import datetime

from banner import *
from Colors import Colors
from Temp import TempPrint

# open('../db/db.json', encoding="utf-8")
try:
    import pandas as pd
    from rich.console import Console
    from rich.table import Table

except ModuleNotFoundError:
    os.system("python install -r requirements.txt")

class Format():
    def date(self):
        output = datetime.now()
        return f"0{output.day}/{output.month}/{output.year}" if output.day < 10 else f"{output.day}/{output.month}/{output.year}"

    def table_list(self, title, status, date):
        table = Table(title="ToDo List")

        table.add_column("Title", justify="left", style="cyan", no_wrap=True)
        table.add_column("Status", justify="center", style="blue")
        table.add_column("Date", justify="center", style="magenta")

        for i in range(1, len(title)+1):
            table.add_row(f"[{i}] - {title[i-1]}", status[i-1], date[i-1])

        console = Console()
        console.print(table)

        # print(len(title)) # ---> 12
        # print(status)
        # print(date)

    def table_options(self):
        table = Table(title="OPTIONS")

        table.add_column("Command", justify="center", style="cyan")
        table.add_column("Descriptions", justify="center", style="blue")

        table.add_row("- c", "Create a new ITEM")
        table.add_row("- u", "Update a ITEM")
        table.add_row("- d", "Delete a ITEM")
        table.add_row("- exit", "Exit the program")

        console = Console()
        console.print(table)

class Main(Format):
    """
        Main program.
    """
    END = False
    
    def __init__(self) -> None:
        os.system('cls')
        while not self.END:
            print(Colors.BLUE + MAIN_BANNER + Colors.END)
            self.read_output_csv()
            print('-' * 50)
            self.table_options()
            function_choice = str(input("Type your choice: ")).lower().strip()
            print('-' * 50)

            if(function_choice == "c"):
                self.create_output_csv()

            elif(function_choice == "u"):
                self.update_output_csv()

            elif(function_choice == "d"):
                self.delete_output_csv()

            elif(function_choice == "exit"):
                print('')
                self.END = True

            else:
                print(Colors.BACK_RED + " ERROR " + Colors.END, end="")
                print(Colors.RED + "This choice don't exists." + Colors.END)
                time.sleep(2)
                

            print('-' * 50)
            print('')

    def create_output_csv(self):
        """
            Insert a new item in Excel file.
        """

        TempPrint(Colors.CYAN + "[+] Creating..." + Colors.END).TPrint()
        print(Colors.BACK_CYAN + " CREATED " + Colors.END, end="")
        print(Colors.CYAN + " [+] NEW ITEM INSERTED SUCCESSYFULLY" + Colors.END)

    def read_output_csv(self):
        """
            Read Excel file.
        """
        # COLUMNS > WEEK DAY
        # ROWS > Escolher Brinquedos/Diversos | Cortar a Grama

        # df = pd.read_csv('Assets/output.csv')
        # print(df.to_string())

        data = open('Assets/output.csv', 'r', encoding="utf-8")
        data_line = data.readline()

        title = []
        status = []
        date = []
        current_line = 1

        while data_line:
            if current_line > 1:
                formated = data_line.split(';')
                title.append(formated[0])
                status.append(formated[1])
                date.append(formated[2].replace('\n', ""))
                # print(f"[{current_line}] - {formated}")

            data_line = data.readline()
            current_line += 1

        data.close()
        self.table_list(title, status, date)

    def update_output_csv(self):
        """
            Update a item in Excel file.
        """

        data = open('Assets/output.csv', 'r', encoding="utf-8")
        print(data.read())
        data.close()

        TempPrint(Colors.CYAN + "[+] Updating..." + Colors.END).TPrint()
        print(Colors.BACK_CYAN + " UPDATED " + Colors.END, end="")
        print(Colors.CYAN + " [+] ITEM UPDATED SUCCESSYFULLY" + Colors.END)
    
    def delete_output_csv(self):
        """
            Delete a item in Excel file.
        """

        data = open('Assets/output.csv', 'r', encoding="utf-8")
        print(data.read())
        data.close()

        TempPrint(Colors.RED + "[+] Deleting..." + Colors.END).TPrint()
        print(Colors.BACK_CYAN + " DELETED " + Colors.END, end="")
        print(Colors.CYAN + " [+] ITEM DELETED SUCCESSYFULLY" + Colors.END)

if __name__ == '__main__':
    Main()
    print("Thanks!!!")
    print(Colors.CYAN + MENU_BANNER + Colors.END)