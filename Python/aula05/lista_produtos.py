produtos = [
    {"nome": "Teclado",   "categoria": "Periféricos", "preco": 150},
    {"nome": "Mouse",     "categoria": "Periféricos", "preco": 80},
    {"nome": "Monitor",   "categoria": "Monitores",   "preco": 480},
    {"nome": "Headset",   "categoria": "Áudio",       "preco": 180},
    {"nome": "Caixa Som", "categoria": "Áudio",       "preco": 90},
    {"nome": "SSD",       "categoria": "Memória",     "preco": 250},
    {"nome": "Mousepad",  "categoria": "Periféricos", "preco": 70},
    {"nome": "Webcam",    "categoria": "Periféricos", "preco": 210},
]

def filtrar_categoria(lista, categoria):
    resultado = []
    for produto in lista:
        if produto["categoria"] == categoria:
            resultado.append(produto)
    return resultado

def filtrar_preco(lista, preco_max):
    resultado = []
    for produto in lista:
        if produto["preco"] <= preco_max:
            resultado.append(produto)
    return resultado

def mostrar(lista):
    if len(lista) == 0:
        print("Nenhum produto encontrado.")
    else:
        for produto in lista:
            print(f"{produto['nome']:<12} - {produto['categoria']:<12} - R${produto['preco']:<12}")
    print(f"Total: {len(lista)} produtos(s)\n")

def existe(lista, nome):
    for produto in lista:
        if produto["nome"].lower() == nome.lower():
            return print("O produto foi encontrado na lista com sucesso!")
    print("O produto não foi encontrado na lista.")


print("=== TODOS OS PRODUTOS ===")
mostrar(produtos)

print("=== PRODUTOS POR CATEGORIA ===")
perifericos = filtrar_categoria(produtos, "Periféricos")
mostrar(perifericos)

print("=== PREÇO ATÉ R$150 ===")
baratos = filtrar_preco(produtos, 150)
mostrar(baratos)

print("=== PERIFÉRICOS ATÉ R$150 ===")
resultado = filtrar_categoria(baratos, "Periféricos")
mostrar(resultado)

verificar_produto = input("Digite o nome do produto que quer verificar: ")
existe(produtos, verificar_produto)