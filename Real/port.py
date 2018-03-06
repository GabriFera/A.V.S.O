__author__ = "Gabriel Laureth Philippi"

"""
PortScan Versão 3.0

OBS: Está função não deve ser executada individualmente, ela faz parte do arquivo inicializador.py

"""

#Imports
import socket, time, os

class Scan:

    portasAbertas = []
    port = [["5", "RJE", "(REMOT JOB ENTRY), Acesso remoto á área de trabalho Habilitada","TCP"],
            ["20", "FTP", "(FILE TRANSFER PROTOCOL), Transferencia de arquivos Habilitada","TCP"],
            ["21", "FTP", "(FILE TRANSFER PROTOCOL), Transferencia de arquivos Habilitada","TCP"],
            ["22", "SSH", "(SECURE SHELL) Acesso Remoto ao computador habilitada","TCP"],
            ["23", "TELNET","Uma Especie de acesso remoto porém com menos funções","TCP"],
            ["25", "SMTP", "Protocolo para envio de e-mails geralmente FAKE","TCP"],
            ["80", "HTTP", "Protocolo WEB geralmente usado pelo APACHE para acesso a arquivos web em seu computador","TCP"],
            ["111", "RPC", "Porta extremamente vulneravel a ataques DDoS","TCP"],
            ["443", "HTTPS", "Porta para servidores WEB","TCP"],
            ["3306", "MYSQL", "Porta usada pelo programa MYSQL","TCP"]]

    def __init__(self, ip):
        self.ip = ip


        """
        Função Para Iniciar o Scan
        """

    def iniciarScan(self):
        print("A.V.I.S.O, Software de analise de vulnerabilidades")
        self.inicio = time.time()
        try:
            print()
            for porta in range(1, 2**16):
                self.sock = socket.socket()
                print("\rScaneando Porta: %s" %(porta), end="")
                resultado = self.sock.connect_ex((self.ip, porta))
                if resultado == 0:
                    self.portasAbertas.append(porta)
            print()
            self.verificarPortas()
            self.fim = time.time()
            print()
            print("Scan finalizado em %i segundos" %(abs(self.fim-self.inicio)))
            print()
            a = input("Enter para sair...")
            os.system("clear")

        except KeyboardInterrupt:
            print()
            print("Scan Cancelado no meio do processo, sem resultados a mostrar")

#            print("Algo Aconteceu, scan não pode ser Inicializado")

    """
    Esta Parte vai verificar se é TCP ou UDP assim como os serviços que estão nela rodadndo
    """
    def verificarPortas(self):
        print()
        print("Scanner Completo")
        print()
        print("Portas Abertas")
        for i in self.portasAbertas:
            verify = False
            for j in self.port:
                if i == int(j[0]):
                    verify = True
                    print("%s/%s - %s" %(j[0], j[3], j[1]))
                    print("    INFORMAÇÕES: %s" %(j[2]))
                    print()

            if not verify:
                print("%s/??? - Serviço Desconhecido" %(i))
                print()
