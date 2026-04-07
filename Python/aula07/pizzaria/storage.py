import json
import os
from pizza import Pizza

ARQUIVO = "pizzas.json"

def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return [Pizza.from_dict(pizza) for pizza in dados]

def salvar(pizzas):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump([pizza.to_dict() for pizza in pizzas], arquivo, indent=4, ensure_ascii=False)