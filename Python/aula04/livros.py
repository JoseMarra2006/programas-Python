livros = [
    "1 - Dom Casmurro - Machado de Assis",
    "2 - 1984 - George Orwell",
    "3 - O Pequeno Príncipe - Antoine de Saint-Exupéry",
    "4 - Cem Anos de Solidão - Gabriel García Márquez",
    "5 - O Senhor dos Anéis: A Sociedade do Anel - J.R.R. Tolkien",
    "6 - Orgulho e Preconceito - Jane Austen",
    "7 - A Hora da Estrela - Clarice Lispector",
    "8 - O Hobbit - J.R.R. Tolkien",
    "9 - Crime e Castigo - Fiódor Dostoiévski",
    "10 - Ensaio Sobre a Cegueira - José Saramago"
]

emprestimos = []

while True:

    print("\n" * 2)
    print("=== LIVROS ===")
    print("1 - Ver livros disponíveis.\n 2 - Emprestar Livro\n 3 - Devolver livro\n 4 - Consultar Empréstimos\n 5 - Sair")
    opcao = input("Digite a opção de livro desejada: ")
    print("\n" * 2)

    if opcao == "1":
            for livro in livros:
                print(livro)
                continue
    elif opcao == "2":
            escolha = int(input(f"Digite o número do livro que deseja: "))
            escolha = escolha - 1
            for i in range(10):
                if livros[i] == escolha:
                    i.remove(livros)
                    i.append(emprestimos)
                    continue
    elif opcao == "3":
        for emprestimo in emprestimos:
              print(emprestimo)
        devolucao = input("Escolha um livro para devolver: ")
        for i in emprestimos:
             if emprestimos[i] == devolucao:
                  i.remove(emprestimos)
                  i.append(livros)
                  continue
    elif opcao == "4":
         for emprestimo in emprestimos:
              print(emprestimo)
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
         print("Código inválido!")
