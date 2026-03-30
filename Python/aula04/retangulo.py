import math

base = float(input("Digite o valor da base do retângulo: "))
altura = float(input("Digite o valor da altura do retângulo: "))

area = base * altura
perimetro = (base * 2) + (altura * 2)
diagonal = math.sqrt(base**2 + altura**2)

input(f"A área do retângulo é igual a: {area:.4f}")
input(f"O perímetro do retângulo é igual a: {perimetro:.4f}")
input(f"A diagonal do retângulo é igual a: {diagonal:.4f}")