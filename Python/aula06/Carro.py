class Carro:

    def __init__(self, marca, modelo, ano, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 10

carro1 = Carro("Volkswagen", "Voyage", "2010", "Preto", 0)
print(carro1.cor)
carro1.acelerar()
print(carro1.velocidade)
carro1.frear()
print(carro1.velocidade)