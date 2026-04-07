def menu():
    while True:
        print("=== PIZZARIA ===")
        print("1. Cadastrar Pizza")
        print("2. Consultar Pizzas")
        print("0. Sair")

        opcao = input("-> ")
        if opcao == "1":
            crud.cadastrar()
        elif opcao == "2":
            crud.consultar()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()