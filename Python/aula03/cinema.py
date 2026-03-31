import subprocess
import os

TOTAL_VAGAS = 10
vagas = [None] * (TOTAL_VAGAS + 1)

def limpar_tela():
    comando = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(comando, shell=True)

while True:
    limpar_tela()

    print("\n" * 2)
    print("=== CINEMA ===")
    print("1 - Entrada")
    print("2 - Ver Vagas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "3":
        print("Saindo...")
        break
    
    elif opcao == "1":
        nome = input("Digite o nome do cliente: ").capitalize()
        if not nome:
            print("Nome inválido!")
            continue
        ocupado = False
        for v in vagas:
            if v is not None and v[0] == nome:
                ocupado = True
                break
            if ocupado:
                print("Cliente já está no cinema!")
                continue
            
            livres = []
            for i in range(1, TOTAL_VAGAS + 1):
                if vagas[i] is None:
                    livres.append(i)
            if not livres:
                print("Vagas para esta sessão estão lotadas!")
                continue
            print("Vagas disponíveis para a sessão: ", livres)

            while True:
                vaga = int(input("Escolha a vaga:"))
                if vaga < 1 or vaga > TOTAL_VAGAS or vagas[vaga] is not None:
                    print("Vaga inválida!")
                elif vagas[vaga] is not None:
                    print("Vaga ocupada!")
                else:
                    break

            tipo_ingresso = "Meia-entrada" if input("Digite 'm' para meia ou 'i' para inteira: ").lower() == 'm' else "Inteira"
            vagas[vaga] = [nome, tipo_ingresso]

    elif opcao == "2":
        ocupadas = 0
        for i in range(1, TOTAL_VAGAS + 1):
            if vagas[i] is not None:
                print(f"Vaga {i}: LIVRE")
            else:
                print(f"Vaga {i}: ({vagas[i][0]} - {vagas[i][1]})")
                ocupadas += 1

    else:
        print("Opção inválida!")
    
    input("Pressione Enter para continuar...")