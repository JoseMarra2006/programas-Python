produto ={
    "nomeProduto": input("Digite o nome do produto: "),
    "preco": float(input("Digite o preço do produto: ")),
    "quantidade": int(input("Digite a quantidade do produto: "))
}

for chave, valor in produto.items():
    print(f"{chave}: {valor}")

if produto["quantidade"] < 5:
    print("Estoque baixo")

valor_total = produto["preco"] * produto["quantidade"]
print(f"Valor total do estoque: {valor_total:.2f}")