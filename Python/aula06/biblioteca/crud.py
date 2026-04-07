from livro import Livro
import storage

def cadastrar():
    livros = storage.carregar()
    
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação do livro: ")

    novo_id = 1 if not livros else livros[-1].id + 1
    livro = Livro(novo_id, titulo, autor, ano)
    livros.append(livro)
    storage.salvar(livros)
    print("Livro cadastrado com sucesso!")

def consultar():
    livros = storage.carregar()
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    
    print("\n Lista de Livros \n")
    print(f"{'ID':<3} | {'Título':<20} | {'Autor':<15} | {'Ano':<3}")
    print("-" * 50)

    for livro in livros:
        print(f"{livro.id:<3} | {livro.titulo:<20} | {livro.autor:<15} | {livro.ano:<3}")
        print("-" * 50)
        
    print()

def excluir():
    livros = storage.carregar()
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    consultar()
    try:
        id_excluir = int(input("Digite o ID do livro a ser excluído: "))
    except ValueError:
        print("ID inválido. Certifique-se de digitar um número inteiro.")
        return
    
    novos = [livro for livro in livros if livro.id != id_excluir]
    if len(novos) == len(livros):
        print("Livro não encontrado.")
    else:
        storage.salvar(novos)
        print("Livro excluído com sucesso!")