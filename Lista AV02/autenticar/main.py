from controlador_usuario import autenticar

login = input("Digite o login: ")
senha = input("Digite a senha: ")

if autenticar(login, senha):
    print("Login realizado com sucesso!")
else:
    print("Login ou senha inválidos.")