num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O número {num1} é maior que {num2}')

elif num2 > num1:
    print(f'O número {num2} é maior que {num1}')

else:
    print(f'Os números {num1} e {num2} são iguais')