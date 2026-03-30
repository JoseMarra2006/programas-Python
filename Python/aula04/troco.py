preco = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
valor_dado = float(input("Digite o valor de pagamento: "))

valor_total = preco * quantidade
troco = valor_dado - valor_total

input(f"O troco voltado foi de: {troco:.2f}")