class ContaBancaria:

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

contaBancaria = ContaBancaria()

def depositar(self, valor):
    self.saldo += valor
    print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")

def sacar(self, valor):
    if valor <= self.saldo:
        self.saldo -= valor
        print(f"Saque no valor de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")
    else:
        print("Saldo insuficiente para o saque.")

def consultar_saldo(self):
    print(f"Saldo atual da conta de {self.titular}: R${self.saldo}")