notas = []

for i in range(4):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("A média é:", media)