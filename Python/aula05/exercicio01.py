def calculo_gasto(salario, gasto):
    if salario > 0 and gasto < salario:
        return print(f"Você tem boas condições financeiras. Seu saldo é de: {salario - gasto}")
    elif salario > 0 and gasto > salario:
        return print(f"Está gastando demais! Seu saldo é de: {salario - gasto}")
    else:
        return print(f"Você não possui salário.")


salario = float(input("Digite o valor do seu salário: "))
gasto = float(input("Digite o valor do seu gasto: "))

calculo_gasto(salario, gasto)