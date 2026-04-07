import crud

def menu():
    while True:
        print("=== SISTEMA DE LIVROS ===")
        print("1. Cadastrar Livro")
        print("2. Consultar Livros")
        print("3. Excluir Livro")
        print("0. Sair")

        opcao = input("-> ")
        if opcao == "1":
            crud.cadastrar()
        elif opcao == "2":
            crud.consultar()
        elif opcao == "3":
            crud.excluir()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()