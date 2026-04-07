import json
import os
from livro import Livro

ARQUIVO = "livros.json"

def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return [Livro.from_dict(livro) for livro in dados]

def salvar(livros):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump([livro.to_dict() for livro in livros], arquivo, indent=4, ensure_ascii=False)