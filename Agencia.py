from random import randint


class Agencia:
    
    def __init__(self, telefone, cnpj, numero):
        
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
    
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa com valor abaixo do esperado. Caixa: R${:,.2f}'.format(self.caixa))
        else:
            print('Caixa com valor ok. Caixa: R${:,.2f}'.format(self.caixa))    
    
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa < valor:
            print('Impossível realizar o empréstimo, pouco dinheiro em caixa.')
        else:
            self.emprestimos.append((valor, cpf, juros))
    
    def cadastrar_cliente(self, nome, cpf, capital):
        self.clientes.append((nome, cpf, capital))


#subclasse da Superclasse Agencia
        
class AgenciaVirtual(Agencia):
    
    
    def __init__(self, site, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = 1000)
        self.site = site
        self.caixa = 1000000
        self.caixa_paypal = 0
    
    
    
    def depositar_paypal(self, valor):
        if self.caixa < valor:
            print('Valor em caixa insuficiente para o depósito. Caixa: R${:,.2f}'.format(self.caixa))
        else:
            self.caixa -= valor
            self.caixa_paypal += valor
    
    
    
    def sacar_paypal(self, valor):
        if self.caixa_paypal < valor:
            print('Valor no caixa PayPal insuficiente para o saque. Caixa PayPal: R${:,.2f}'.format(self.caixa_paypal))
        else:
            self.caixa += valor
            self.caixa_paypal -= valor
 
 
    
#subclasse da Superclasse Agencia
class AgenciaComun(Agencia):
   
   def __init__(self, telefone, cnpj):
       super().__init__(telefone, cnpj, numero = randint(1001,9999))
       self.caixa = 1000000



#subclasse da Superclasse Agencia
class AgenciaPremiun(Agencia):
    
    def __init__(self, telefone, cnpj):
       super().__init__(telefone, cnpj, numero = randint(1001,9999))
       self.caixa = 10000000
       
    def cadastrar_cliente(self, nome, cpf, capital):
        if capital > 1000000:
            super().cadastrar_cliente(nome, cpf, capital)
        else:
            print('Cliente com capital minímo insuficiente para a Agencia Premiun.')