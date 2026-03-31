def saudacao():
    print(f"Olá, seja bem vindo! {printarNome()}")


def printarNome():
    nome = input("Qual seu nome: ")
    print(f"Olá, {nome}")
    return nome

saudacao()

