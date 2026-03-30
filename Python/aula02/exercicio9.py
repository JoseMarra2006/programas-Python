numeros = []

numeros_pares = []

for i in range(10):
    input_numero = int(input("Digite um número: "))
    numeros.append(input_numero)

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

count_pares = len(numeros_pares)

print(f"Números digitados: {numeros}")
print(f"Números pares: {numeros_pares}")
print(f"Quantidade de números pares: {count_pares}")
