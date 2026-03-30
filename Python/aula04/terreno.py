largura = float(input("Digite a largura do terreno desejado: "))
comprimento = float(input("Digite o comprimento do terreno desejado: "))

preco = float(input("Digite o preço do metro quadrado (m²) do terreno desejado: "))

area = largura * comprimento
preco_total = area * preco

print(f"Área total do terreno: {area:.2f}")
print(f"Preço total do terreno: {preco_total:.2f}")
