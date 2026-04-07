import storage
from pizza import Pizza

SABORES_PERMITIDOS = ["calabresa", "parmegiana", "portuguesa"]

def cadastrar():
    print(f"Sabores disponíveis: {', '.join(SABORES_PERMITIDOS)}")
    sabor = input("Digite o sabor da pizza: ").lower()
    
    while sabor not in SABORES_PERMITIDOS:
        print("Sabor inválido! Escolha uma das opções disponíveis.")
        sabor = input("Digite o sabor da pizza: ").lower()

    tamanho = input("Digite o tamanho da pizza: ")
    massa = input("Digite o tipo da massa: ")
    
    nova_pizza = Pizza(sabor, tamanho, massa)
    
    pizzas = storage.carregar()
    pizzas.append(nova_pizza)
    storage.salvar(pizzas)
    
    print("Pizza cadastrada com sucesso!\n")

def consultar():
    pizzas = storage.carregar()
    
    if not pizzas:
        print("Nenhuma pizza cadastrada no momento.\n")
        return
        
    print("\n--- Pizzas Cadastradas ---")
    for i, pizza in enumerate(pizzas, 1):
        print(f"{i}. Sabor: {pizza.sabor.capitalize()} | Tamanho: {pizza.tamanho} | Massa: {pizza.massa}")
    print("--------------------------\n")