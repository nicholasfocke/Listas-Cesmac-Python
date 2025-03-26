
while True:
    try:
        idade = int(input("Digite sua idade: "))
        nome = input("Digite sua idade: ")
        print(f"Seu nome é {nome} e sua idade é {idade} anos")
        break

    except ValueError:
        print("Digite um nome e um valor inteiro!!")