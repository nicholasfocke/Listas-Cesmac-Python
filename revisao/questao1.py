num  = int(input("Digite um valor inteiro: "))

numeros_pares = []
numeros_impares = []


for i in range(1, num + 1):
    if i % 2 == 0:
        numeros_pares.append(i)
    else:
        numeros_impares.append(i)

print(f'Numeros pares:', *numeros_pares, sep=" ")
print(f'\nNumeros impares: ',*numeros_impares, sep=" ")