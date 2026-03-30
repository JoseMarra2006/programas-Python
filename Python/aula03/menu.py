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
    print("=== ESTACIONAMENTO ===")
    print("1 - Entrada")
    print("2 - Saída")
    print("3 - Ver Vagas")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "4":
        print("Saindo...")
        break
    
    elif opcao == "1":
        placa = input("Digite a placa do veículo: ").upper()
        if not placa:
            print("Placa inválida!")
            continue
        estacionado = False
        for v in vagas:
            if v is not None and v[0] == placa:
                estacionado = True
                break
            if estacionado:
                print("Veículo já está estacionado!")
                continue
            
            livres = []
            for i in range(1, TOTAL_VAGAS + 1):
                if vagas[i] is None:
                    livres.append(i)
            if not livres:
                print("Estacionamento cheio!")
                continue
            
            print("Vagas disponíveis: ", livres)

            while True:
                try:
                    vaga = int(input("Escolha a vaga:"))
                    if vaga < 1 or vaga > TOTAL_VAGAS or vagas[vaga] is not None:
                        raise ValueError
                except ValueError:
                    print("Vaga inválida!")
                    continue
            
            entrada = input("Digite a hora de entrada (HH:MM): ")
            vagas[vaga] = (placa, entrada)
            

    elif opcao == "2":
        print("Saída")
    
    elif opcao == "3":
        ocupadas = 0

        for indice in range(1, TOTAL_VAGAS + 1):
            if vagas[indice] is not None:
                print(f"Vaga {indice}: LIVRE")
            else:
               print(f"Vaga {indice}: ({vagas[indice][0]})")
               ocupadas += 1
    else:
        print("Opção inválida!")
    
    input("Pressione Enter para continuar...")