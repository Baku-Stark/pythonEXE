"""
    Exercício do curso Trilha Digital | Web Pack Back-End
"""

try:
    import os
    from time import sleep

    class CASH_MACHINE():
        """
            Profile
            ----------
            Author : Baku - Stark
            Info   : Classe principal da aplicação.
            About  : Exercício do curso Trilha Digital | Web Back-End
        """

        RED =       '\033[31m'
        GREEN =     '\033[32m'
        YELLOW =    '\033[33m'
        BLUE =      '\033[34m'
        PURPLE =    '\033[35m'
        CYAN =      '\033[36m'
        WHITE =     '\033[37m'
        GRAY =      '\033[90m'
        END =       '\033[m'

        saldo = 0
        deposito = 0

        end_program = False

        def __init__(self):
            os.system('cls')
            self.banner()
            self.menu()

        def banner(self):
            print(
                self.CYAN +
                """
                     _      _____ _     ____  ____  _      _____
                    / \  /|/  __// \   /   _\/  _ \/ \__/|/  __/
                    | |  |||  \  | |   |  /  | / \|| |\/|||  \  
                    | |/\|||  /_ | |_/\|  \_ | \_/|| |  |||  /_ 
                    \_/  \|\____\ \____/\____/\____/\_/  \|\____\
                """
                + self.END
            )

        def menu(self):
            """
                Menu para escolha das opções.
            """
            
            while not self.end_program:
                print(
                    self.BLUE +
                    """
                        Escolha uma das seguintes opções
                            [A] --> SALDO
                            [B] --> DEPOSITAR
                            [C] --> SAQUE
                            [D] --> SAIR
                    """
                    + self.END
                )

                select_opt = str(input('r: ')).upper()
                sleep(1)
                print('')

                if select_opt == 'A':
                    self.caixa_saldo()
                    print('\n' * 3)

                elif select_opt == 'B':
                    os.system('cls')
                    self.caixa_depositar()

                elif select_opt == 'C':
                    os.system('cls')
                    self.caixa_saque()

                elif select_opt == 'D':
                    print('\033[41m' + ' INFO ' + '\033[m', end="")
                    print(self.RED + ' Programa finalizado!!!' + self.END)
                    self.end_program = True

                else:
                    print('\033[45m' + ' INFO ' + '\033[m', end="")
                    print(self.PURPLE + ' Opção inválida!' + self.END)
                
                sleep(2)
                os.system('cls')

        def caixa_saldo(self):
            """
                Mostrar saldo ao usuário.
            """

            saldo_str = f"{self.saldo:.2f}"

            print("=" * 50)
            print(self.BLUE + f"Seu saldo é de R${saldo_str.replace('.', ',')}".center(50) + self.END)
            print("=" * 50)
            print('')

        def caixa_depositar(self):
            """
                Depositar quantia no caixa.
            """

            print("=" * 50)
            print(self.BLUE + "REALIZAR DEPÓSITO!".center(50) + self.END)
            print("=" * 50)
            print('')

            check = False

            while not check:
                try:
                    deposito_qtd = float(input('Digite a quantia que deseja depositar \nR$: '))

                    if deposito_qtd < 0:
                        print(self.RED + "[!] VALOR INCORRETO PARA SAQUE!" + self.END)

                    else:
                        print(self.GREEN + "[!] DEPÓSITO REALIZADO COM SUCESSO!" + self.END)
                        self.deposito += deposito_qtd
                        self.saldo = self.deposito
                        check = True

                    print('')

                except ValueError:
                    print(self.RED + "[!] ERROR [!]" + self.END)
                    print('\n' * 3)


        def caixa_saque(self):
            """
                Realizar uma determinada quantia para saque.
            """

            print("=" * 50)
            print(self.BLUE + "REALIZAR SAQUE!".center(50) + self.END)
            print("=" * 50)
            print('')

            check = False

            while not check:
                try:
                    saque = float(input('Quantia do saque \nR$: '))

                    if saque > self.deposito:
                        print(self.RED + "[!] VOCÊ NÃO POSSUI ESSE SALDO... [!]" + self.END)

                    else:
                        self.deposito -= saque
                        self.saldo = self.deposito
                        print(self.GREEN + "[!] SAQUE REALIZADO COM SUCESSO!" + self.END)
                        check = True
                    
                    print('')

                except ValueError:
                    print(self.RED + "[!] ERROR [!]" + self.END)
                    print('\n' * 3)

except Exception:
    print(Exception)

except KeyboardInterrupt:
    print('\033[90;44m' + 'INFO' + '\033[m', end="")
    print('Programa finalizado (KeyboardInterrupt)')

finally:
    if __name__ == '__main__':
        CASH_MACHINE()