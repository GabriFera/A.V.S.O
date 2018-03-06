import os, time, socket
from port import *

__author__ = "Gabriel Laureth Philippi"

"""
Inicializador do A.V.I.S.O

O codigo será dividido em um arquivo para cada função, onde todos eles se encontrão aqui

"""

class Inicializador():

    """
    IP deve sempre permanecer o IP local ao menos que seja necessario escanear outro computador que não seja este
    """
    IP = "127.0.0.1"

    def PortScan(self):
        port = Scan(self.IP)
        port.iniciarScan()

if __name__ == "__main__":
    os.system("clear")
    i = Inicializador()
    while True:
        print(
    """
A.V.I.S.O

Escolha uma das Opções

1 - Escanear Portas (1 - 65535)
99 - Sair

Mais Funções Estão Por Vir!!!
    """
        )
        a = input("Escolha uma das opções acima: ")
        if a == "1":
            os.system("clear")
            i.PortScan()
        elif a == "99":
            quit()
            break
        else:
            print("Função Indisponivel")
