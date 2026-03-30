preco = [5.00, 3.50, 4.80, 8.90, 7.32]

codigo = int(input("Código do produto comprado (1 a 5): "))

qtd = int(input("Quantidade comprada: "))

pagar = 0

if 1 <= codigo <= 5:
    pagar = qtd * preco[codigo-1]
    print(f"Valor a pagar: R$ {pagar:.2f}")
else:
    print("Código inválido!")