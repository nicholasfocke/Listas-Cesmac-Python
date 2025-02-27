while True:
    nome = input("Digite seu nome completo: ")

    if len(nome) > 3:
        break

    print("Erro! O nome deve ter mais de 3 caracteres.")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
            break

        print("Erro! A idade deve estar entre 0 e 150.")

    except ValueError:
        print("Erro! Digite um número inteiro para a idade.")

while True:
    try:
        salario = float(input("Digite seu salário: "))
        if salario > 0:
            break

        print("Erro! O salário deve ser maior que zero.")

    except ValueError:
        print("Erro! Digite um valor numérico válido para o salário.")

while True:
    sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").lower()

    if sexo in ('f', 'm'):
        break

    print("Erro! O sexo deve ser 'f' ou 'm'.")

while True:
    estado_civil = input("Digite seu estado civil ('s' - solteiro, 'c' - casado, 'v' - viúvo, 'd' - divorciado): ").lower()

    if estado_civil in ('s', 'c', 'v', 'd'):
        break

    print("Erro! O estado civil deve ser 's', 'c', 'v' ou 'd'.")

if estado_civil == 's':
    estado_civil = 'Solteiro'

elif estado_civil =='c':
    estado_civil = 'Casado'

elif estado_civil == 'v':
    estado_civil = 'Viúvo'

else:
    estado_civil = 'Divorciado'


print("\nInformações cadastradas com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
print(f"Estado Civil: {estado_civil}")
