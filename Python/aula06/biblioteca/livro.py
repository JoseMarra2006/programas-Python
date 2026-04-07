class Livro:
    def __init__(self, id, titulo, autor, ano):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'ano': self.ano
        }

    @staticmethod
    def from_dict(dados):
        return Livro(
            dados['id'], 
            dados['titulo'], 
            dados['autor'], 
            dados['ano']
        )








# livro1 = Livro()
# titulo = input("Digite o título do livro: ")
# autor = input("Digite o autor do livro: ")
# ano = input("Digite o ano de publicação do livro: ")

# livro1 = Livro(titulo, autor, ano)

# def exibir_informacoes(self):
#     print(f"Título: {self.titulo}")
#     print(f"Autor: {self.autor}")
#     print(f"Ano de Publicação: {self.ano}")

# exibir_informacoes(livro1)