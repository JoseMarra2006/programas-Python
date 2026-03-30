for i in range(20):
    idades = {
        "idade{i+1}": int(input(f"Digite a idade da pessoa {i+1}: ")),
    }

media_idades = sum(idades["idade{i+1}"] for i in range(20)) / len(idades)
print(f"A média das idades é: {media_idades}")