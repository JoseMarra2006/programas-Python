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
    print("1 - Ver livros disponíveis\n2 - Emprestar Livro\n3 - Devolver livro\n4 - Consultar Empréstimos\n5 - Sair")
    opcao = input("Digite a opção de livro desejada: ")
    print("\n" * 2)

    if opcao == "1":
        if not livros:
            print("Não há livros disponíveis no momento.")
        else:
            for livro in livros:
                print(livro)
                
    elif opcao == "2":
        if not livros:
            print("Todos os livros já foram emprestados.")
        else:
            for livro in livros:
                print(livro)
            escolha = input("Digite o número do livro que deseja (ex: 1): ")
            
            livro_encontrado = False
            for livro in livros:
                if livro.startswith(escolha + " -"):
                    emprestimos.append(livro)
                    livros.remove(livro)
                    print(f"Você emprestou: {livro}")
                    livro_encontrado = True
                    break
            
            if not livro_encontrado:
                print("Livro não encontrado ou já emprestado.")

    elif opcao == "3":
        if not emprestimos:
            print("Não há livros para devolver.")
        else:
            for emprestimo in emprestimos:
                print(emprestimo)
            devolucao = input("Digite o número do livro para devolver: ")
            
            livro_encontrado = False
            for livro in emprestimos:
                if livro.startswith(devolucao + " -"):
                    livros.append(livro)
                    emprestimos.remove(livro)
                    livros.sort()
                    print(f"Você devolveu: {livro}")
                    livro_encontrado = True
                    break
            
            if not livro_encontrado:
                print("Este livro não consta na sua lista de empréstimos.")

    elif opcao == "4":
        if not emprestimos:
            print("Nenhum empréstimo ativo.")
        else:
            for emprestimo in emprestimos:
                print(emprestimo)
                
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Código inválido!")