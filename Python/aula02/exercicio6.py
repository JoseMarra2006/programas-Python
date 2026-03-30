alunos = []

aluno1 = {
    "nome": input("Digite o nome do aluno: "),
    "nota1": float(input("Digite a primeira nota do aluno: ")),
    "nota2": float(input("Digite a segunda nota do aluno: "))
}
alunos.append(aluno1)

aluno2 = {
    "nome": input("Digite o nome do aluno: "),
    "nota1": float(input("Digite a primeira nota do aluno: ")),
    "nota2": float(input("Digite a segunda nota do aluno: "))
}
alunos.append(aluno2)

aluno3 = {
    "nome": input("Digite o nome do aluno: "),
    "nota1": float(input("Digite a primeira nota do aluno: ")),
    "nota2": float(input("Digite a segunda nota do aluno: "))
}
alunos.append(aluno3)

for aluno in alunos:
    media = (aluno["nota1"] + aluno["nota2"]) / 2
    print(f"{aluno['nome']} - Média: {media:.2f}")
    if media >= 7.0:
        print("Situação: Aprovado")
    elif media >= 5.0:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")