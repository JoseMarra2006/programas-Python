frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

buscarFruta = input("Qual fruta? ")

resultado = False

if buscarFruta in frutas:
    resultado = True

if resultado:
    print(buscarFruta, "encontrado")
else:    
    print(buscarFruta, "não encontrado")

frutas.sort(reverse=True)

for fruta in frutas:
    print(fruta)