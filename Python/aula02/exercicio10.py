usuarios = {
    "admin": "admin123",
    "joao": "joao456",
    "maria": "maria789"
}

username = input("Digite seu nome de usuário: ")
if username in usuarios:
    password = input("Digite sua senha: ")
    if password == usuarios[username]:
        print("Login bem-sucedido!")
    else:
        print("Senha incorreta.")
else:
    print("Usuário não encontrado.")