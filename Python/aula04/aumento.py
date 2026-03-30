salario = float(input("Digite o salário a ser calculado: "))
 
if salario < 0:
    print("Valor inválido!")

elif salario <= 1000:
    salario_novo = salario + ((20 / 100) * salario)
    aumento = ((20 / 100) * salario)
    print(f"Novo salário: R${salario_novo:.2f}\n Aumento: R${aumento:.2f}\n Porcentagem: 20%")

elif salario > 1000 and salario <= 3000:
    salario_novo = salario + ((15 / 100) * salario)
    aumento = ((15 / 100) * salario)
    print(f"Novo salário: R${salario_novo:.2f}\n Aumento: R${aumento:.2f}\n Porcentagem: 15%")

elif salario > 3000 and salario <= 8000:
    salario_novo = salario + ((10 / 100) * salario)
    aumento = ((10 / 100) * salario)
    print(f"Novo salário: R${salario_novo:.2f}\n Aumento: R${aumento:.2f}\n Porcentagem: 10%")
    
else:
    salario_novo = salario + ((5 / 100) * salario)
    aumento = ((5 / 100) * salario)
    print(f"Novo salário: R${salario_novo:.2f}\n Aumento: R${aumento:.2f}\n Porcentagem: 5%")