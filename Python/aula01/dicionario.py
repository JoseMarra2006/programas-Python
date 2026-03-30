aluno = {
    "nome": "Carlos",
    "idade": 25,
    "nota": 8.5,
}

print("Aluno:", aluno["nome"])
print("Nota:", aluno["nota"])


for chave, valor in aluno.items():
    print(chave, ":", valor)