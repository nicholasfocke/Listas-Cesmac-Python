while True:
    try:
        n = int(input("Quantos números você deseja inserir?: "))
        if n <= 0 or n > 1000:

            print("Quantidade inválida! Digite um número entre 1 e 1000.")
            continue
        break  
  
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

numeros = []  

for i in range(n):
    while True:
        try:
            num = int(input(f"Digite um número: "))
            numeros.append(num)
            break  
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")


maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)


print()
print(f'- O maior número foi {maior}')
print(f'- O menor número foi {menor}')
print(f'- A soma foi {soma}')