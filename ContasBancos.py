from datetime import datetime
import pytz
from random import randint

class ContaCorrente():
    
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, conta) -> None:
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self.limite = None
        self.agencia = agencia
        self.conta = conta
        self.historico = []
        self.cartoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de: R${:,.2f}'.format(self._saldo))
    
    def adicionar_saldo(self,valor):
        self._saldo += valor
        self.historico.append(('Valor depositado: R${:,.2f}'.format(valor),'Saldo: R${:,.2f}'.format(self._saldo), ContaCorrente._data_hora()))
    
    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não pode retirar esta quantidade de dinheiro')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self.historico.append(('Valor Retirado: R${:,.2f}'.format(valor),'Saldo: R${:,.2f}'.format(self._saldo), ContaCorrente._data_hora()))
    
    def consultar_saldo_limite_especial(self):
        print('Seu saldo especial é de : R${:,.2f}'.format(self.__limite_conta()))
    
    def visualizarhistorico(self):
        print('Histórico de transações:')
        print('-' * 80)
        for historico in self.historico:
            print(historico)
            print('-' * 80)
    
    def transeferir(self, valor, conta):
        if self._saldo < valor:
            print('Saldo insuficiente para efetuar a transferencia.')
            print(self.consultar_saldo())
        else:
            self._saldo -= valor
            self.historico.append(('Valor Transferido: R${:,.2f}'.format(valor),'Saldo: R${:,.2f}'.format(self._saldo), ContaCorrente._data_hora()))
            conta._saldo += valor
            conta.historico.append(('Valor Recebido: R${:,.2f}'.format(valor),'Saldo: R${:,.2f}'.format(conta._saldo), ContaCorrente._data_hora()))

class CartaoCredito():
    
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br
    
     
    def __init__(self, titular, conta_corrente):
        
        self.numero = randint(1000000000000000,9999999999999999)
        self.titular = titular
        self.validade = '{:2}/{:2}'.format(CartaoCredito._data_hora().month,CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9),randint(0,9),randint(0,9))
        self.conta_corrente = conta_corrente
        self.limite = 1000
        self._senha = '1234'
        conta_corrente.cartoes.append(self)
     
    @property   
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self,valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor        



