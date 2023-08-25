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
        return f"{output.month}/{output.day}/{output.year}"

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
            print(Colors.BLUE + "OPTIONS" + Colors.END)
            print("[-c] > Create a new ITEM\n[-u] > Update a ITEM\n[-d] > Delete a ITEM\n[-e] > Exit the program\n")
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
        CHECK = False
        
        while not CHECK:
            task = str(input("Task you want to accomplish\nr: ")).strip()
            print('')
            status = "In Progress"
            print('')

            if len(task) > 0:
                write_file = open('Assets/output.csv', 'a+', encoding="utf-8")
                write_file.write(f"{task};{status};{self.date()}\n")

                TempPrint(Colors.CYAN + "[+] Creating..." + Colors.END).TPrint()
                print(Colors.BACK_CYAN + " CREATED " + Colors.END, end="")
                print(Colors.CYAN + " [+] NEW ITEM INSERTED SUCCESSYFULLY" + Colors.END)
                CHECK = True

            else:
                TempPrint(Colors.CYAN + "[+] Creating..." + Colors.END).TPrint()

                print(Colors.BACK_RED + " ERROR " + Colors.END, end="")
                print(Colors.RED + " [+] Try Again..." + Colors.END)

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

        id_choice = int(input("Type title ID: "))
        
        data = open('Assets/output.csv', 'r', encoding="utf-8")
        c_line = 1
        replaced_content = ""

        #looping through the file
        for line in data:
            if c_line > 1:
                if id_choice == c_line-1:
                    print(f"{c_line-1}. {line}")
                    
                    # line to list
                    line = line.split(";")
                    print(f"---> {c_line-1}. {line}")

                    if line[1] == "In Progress":
                        line[1] = "Check"
                    else:
                        line[1] = "In Progress"


                    print(replaced_content)
            replaced_content = f"{line[0]};{line[1]};{line[2]}"
            c_line += 1
        data.close()

        # #Open file in write mode
        # write_file = open("note.txt", "w")

        # #overwriting the old file contents with the new/replaced content
        # write_file.write(replaced_content)

        # #close the file
        # write_file.close()

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