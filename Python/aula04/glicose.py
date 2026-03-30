quant_glicose = float(input("Digite a quantidade de glicose presente no sangue: "))

if quant_glicose <= 0:
    print("Valor inválido")
elif quant_glicose <= 100:
    print("Normal")
elif quant_glicose > 100 and quant_glicose <= 140:
    print("Elevado")
else:
    print("Diabético")