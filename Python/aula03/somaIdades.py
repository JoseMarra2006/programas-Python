for i in range(20):
    idades = {
        "nome": input(f"Digite o nome da pessoa {i+1}: "),
        f"idade{i+1}": int(input(f"Digite a idade da pessoa {i+1}: ")),
    }

soma_idades = sum(idades[f"idade{i+1}"] for i in range(20))
print(f"A soma das idades é: {soma_idades}")