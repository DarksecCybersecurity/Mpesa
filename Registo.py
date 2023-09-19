#################### M-pesa System ###################
from datetime import datetime
from getpass import getpass
#from db import DB

# Criar Classe:
    # Criar Funcao:

class Conta:
    #db = DB()

    #Construtor
    def __init__(self):
        self.nome = "Helton"
        self.pin = "123456"
        self.contacto = ''
        self.codigo_agente = '012345'
        self.saldo = 0

    #Login Autenticacao
    def Login(self):
        try:
            nome = input("Digite seu user: ")
            if nome == self.nome:
                pin = getpass("Digite seu pin: ")
                if pin == self.pin:
                #id = int(input("Digite Id: "))
                #self.db.Insert(id,nome, pin)                        
                    self.Menu()    
                else:
                    print("Usuario invalido!")
            else:
                print("Usuario nao Existe!")
        except Exception as e:
            print(e).close()
           

    #Menu Inicial
    def Menu(self):
        print('-' * 60)
        print(f'                      MOVE CASH')
        print('-' * 60)
        while True:
            open = input("""\n Digite a opcao que deseja: 
            \r 1. Tranferencia
            \r 2. Levantar
            \r 3. Consultar
            \r 4. Depositar
            \r 5. Txenekar
            \r 6. Sair
            \r Entrar: """).upper()

            if open == '6':
                exit()

            #Transferir Dinheiro
            if open == '1':
                while True:
                    open = input("""\n Transferir Dinheiro
                    \r 1. Carteira do Agente
                    \r 2. Carteira do Cliente
                    \r 3. Carteira da Agencia
                    \r 4. voltar
                    \r 5. Sair
                    \r Entrar: """).upper()

                    if open == '1':
                        try:
                            codigo_agente = input("Digite Codigo do agente: ")
                            if codigo_agente == self.codigo_agente:
                                self.valor = float(input("Digite o valor: "))
                                #self.db.Insert(codigo_agente)                        
                                self.Transferir(self.valor)
                                self.data = str(datetime.now())
                                print(self.data)
                                self.ConsultarSaldo(self.valor)
                            else:
                                print("Codigo invalido!")
                        except Exception as e:
                            print(e).close()

                    elif open == '4':
                        self.Menu()
                    elif open == '5':
                        exit()

            #Levantar Dinheiro
            if open == '2':
                while True:
                    open = input("""\n  Levantar 
                    \r 1. Agente
                    \r 2. Agencia
                    \r 3. Voltar
                    \r Entrar: """).upper()

                    if open == '1':
                        try:
                            codigo = input("Digite codigo do agente: ")
                            if codigo == self.codigo_agente:
                                self.valor = float(input("Digite o valor: "))
                                #self.db.Insert(codigo_agente)                        
                                self.Levantar(self.valor)
                                print(f'Confirmado levantou {self.valor:.2f} no agente {self.codigo_agente} {self.nome}')
                                self.data = str(datetime.now())
                                print(self.data)
                                self.ConsultarSaldo(self.valor)
                            else:
                                print("Codigo invalido!")
                        except Exception as e:
                            print(e).close()

                    elif open == '3':
                        self.Menu()

            #Consultar Saldo
            if open == '3':
                self.ConsultarSaldo(self.valor)
                 

    #Transferir Dinheiro
    def Transferir(self, valor):
        try:
            self.saldo += valor
            print('\n')
            print("Transferencia efetuada com sucesso!")
            print(f'Confirmado Recebeu {valor:.2f} do agente {self.codigo_agente} {self.nome}')
        except Exception as e:
            print(e).close()

    #Levantar Dinheiro
    def Levantar(self, valor):
        try:
            if valor <= self.saldo:
                self.saldo -= valor
        except Exception as e:
            print(e)

    #Consultar Saldo!
    def ConsultarSaldo(self, valor):
        try:
            if self.saldo <= valor:
                self.saldo -= valor
                print(f'Seu Saldo e MZN {valor:.2f}')
            else:
                print("Sem saldo!")
        except Exception as e:
            print(e).close()
            
    #Consultar Movimentos
    def ConsultarMovimento(self):
        if len(self.saldo) == 0:
            print('\n Sem Transacoes!')
            return
        print('\n Transacoes Efetuadas: ')

        for self.saldo in sorted(
            self.valor.values(),
            #criar uma lista de ultimas transacoes
            key=lambda transacao: str(transacao["identificador"]),
            reverse=True):

            print(f'{self.saldo} - - : MZN{self.valor:.2f}')

    #Fazer Emprestimo
    def Emprestimo():
        pass

        

conta = Conta()
conta.Login()

conta.Transferir()

conta.Levantar()

conta.ConsultarSaldo()

conta.ConsultarMovimento()