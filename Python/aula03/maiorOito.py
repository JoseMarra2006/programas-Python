numeros = []
numeros_maiores = []

for i in range(5):
    numero = int(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

for numeral in numeros:
    if numeral > 8:
        numeros_maiores.append(numeral)

print(f"Os números maiores que 8 são: {numeros_maiores} e a quantidade de números maiores que 8 é: {len(numeros_maiores)}")