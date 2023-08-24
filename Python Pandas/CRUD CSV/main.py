import os
from banner import *
from Colors import Colors
from Temp import TempPrint

# open('../db/db.json', encoding="utf-8")
try:
    import pandas as pd

except ModuleNotFoundError:
    os.system("python install -r requirements.txt")

class Main():
    """
        Main program.
    """
    END = False
    
    def __init__(self) -> None:
        os.system('cls')
        while not self.END:
            print(Colors.BLUE + MAIN_BANNER + Colors.END)
            self.read_output_csv()
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
                break

            else:
                print(Colors.BACK_RED + " ERROR " + Colors.END, end="")
                print(Colors.RED + "This choice don't exists." + Colors.END)
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
        # ROWS > Escolher Brinquedos/Diversos | Varrer

        # df = pd.read_csv('Assets/output.csv')
        # print(df.to_string())

        data = open('Assets/output.csv', 'r', encoding="utf-8")
        data_line = data.readline()
        current_line = 1
        while data_line:
            print(data_line)
            data_line = data.readline()
        data.close()

    def update_output_csv(self):
        """
            Update a item in Excel file.
        """

        data = open('Assets/output.csv', 'r', encoding="utf-8")
        print(data.read())
        data.close()
    
    def delete_output_csv(self):
        """
            Delete a item in Excel file.
        """

        data = open('Assets/output.csv', 'r', encoding="utf-8")
        print(data.read())
        data.close()

if __name__ == '__main__':
    Main()
    print("Thanks!!!")
    print(Colors.CYAN + MENU_BANNER + Colors.END)