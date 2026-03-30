numeros = []

for i in range(10):
    input_numero = int(input("Digite um número: "))
    numeros.append(input_numero)

print(f"O maior número é: {max(numeros)}")
print(f"O menor número é: {min(numeros)}")
print(f"A média dos números é: {sum(numeros) / len(numeros):.2f}")