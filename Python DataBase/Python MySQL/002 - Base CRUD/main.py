import os, mysql.connector, platform
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()
sys_op = platform.system()

from services.__COLORS import Colors
from services.__TempPrint import TempPrint

def clear_prompt():
    return os.system('cls') if sys_op == 'Windows' else os.system('clear')

class MYSQL_CRUD():
    con = mysql.connector.connect(
        host = os.getenv("MYSQL_ROOT"),
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSQL_PASS"),
        database = os.getenv("MYSQL_DB")
    )
    cursor = con.cursor()

    user_choice = 0

    def __init__(self):
        super().__init__()

        while self.user_choice < 5:
            # === OPTION MENU
            print(
                Colors.CYAN + """
                    [ 1 ] - Create new Item
                    [ 2 ] - Read Table
                    [ 3 ] - Update
                    [ 4 ] - Delete
                    [ 5 ] - Finish Program
                """ + Colors.END
            )
            print('-' * 50)

            self.user_choice = int(input("Choose an option above: "))
            print('')

            if self.user_choice < 1:
                msg = Colors.RED + "[-] Try again..." + Colors.END
                TempPrint(msg).TPrint()
                clear_prompt()

            else:
                if self.user_choice == 1:
                    self.create_db()

                elif self.user_choice == 2:
                    self.read_db()

                elif self.user_choice == 3:
                    self.update_db()

                elif self.user_choice == 4:
                    self.delete_db()

                else:
                    print(Colors.BACK_CYAN + "GOOD BYE!" + Colors.END)
                
                print('')
                print('-' * 50)
                

        # === END PROGRAM
        self.cursor.close()
        self.con.close()

    def create_db(self):
        nome_produto = str(input("Car name: ")).strip().capitalize()
        print('')

        valor = int(input("Car price R$"))
        print('')

        self.cursor.execute(f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})')
        self.con.commit()
        print(Colors.BACK_CYAN + "NEW CAR!" + Colors.END)

    def read_db(self):
        self.cursor.execute("SELECT * FROM bdyoutube.vendas")
        data = self.cursor.fetchall()

        for item in data:
            print(item)

    def update_db(self):
        print("Update info")
        self.read_db()
        print('')

        choice_id = int(input("Car ID: "))
        print('')

        n_nome_produto = str(input("Car name: ")).strip().capitalize()
        print('')

        n_valor = int(input("Car price R$"))
        print('')

        if len(n_nome_produto) > 0 and len(str(n_valor)) == 0:
            self.cursor.execute(f"UPDATE bdyoutube.vendas SET nome_produto = '{n_nome_produto}' WHERE (idvendas = {choice_id})")

        elif len(n_nome_produto) == 0 and len(str(n_valor)) > 0:
            self.cursor.execute(f"UPDATE bdyoutube.vendas SET valor = {n_valor} WHERE (idvendas = {choice_id})")

        else:
            self.cursor.execute(f"UPDATE bdyoutube.vendas SET nome_produto = '{n_nome_produto}', valor = {n_valor} WHERE (idvendas = {choice_id})")

        self.con.commit()
        print(Colors.BACK_CYAN + "UPDATED!" + Colors.END)

    def delete_db(self):
        print("Delete info")
        self.read_db()
        print('')

        choice_id = int(input("Car ID: "))
        print('')

        self.cursor.execute(f"DELETE FROM bdyoutube.vendas WHERE (idvendas = {choice_id})")

        self.con.commit()
        print(Colors.BACK_CYAN + "DELETED!" + Colors.END)

if __name__ == '__main__':
    clear_prompt()
    MYSQL_CRUD()