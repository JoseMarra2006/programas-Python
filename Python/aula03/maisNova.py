nome_mais_novo = ""
menor_idade = 999

for i in range(3):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))

    if idade < menor_idade:
        menor_idade = idade
        nome_mais_novo = nome

print(f"A pessoa mais nova é: {nome_mais_novo} com a idade de {menor_idade} anos.")