frutas = ["Mamão", "Uva", "Pêra"]
aluno = ["Carlos", 25, 75.5, "M", True]
pesos = [14.3, 18.7, 19, 21.8, 1]

print(frutas)
print(aluno[0])
print("Peso: ", pesos[2])

frutas.append("Abacaxi")
print(frutas)

aluno.insert(2, "Engenharia")
print(aluno)
pesos.remove(19)
print(pesos)

frutas.pop(1)
for fruta in frutas:
    print(fruta)

if "Pêra" in frutas:
    print("A fruta Pêra está na lista.")
else:    
    print("A fruta Pêra não está na lista.")