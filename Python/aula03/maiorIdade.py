idades_maiores = []
idades = []

for i in range(5):
    idades.append(int(input(f"Digite a idade da pessoa {i+1}: ")))

print(idades)

for idade in idades:
    if idade >= 18:
        idades_maiores.append(idade)

print(f"As idades maiores de idade são: {idades_maiores} e a quantidade de pessoas maiores de idade é: {len(idades_maiores)}")