while True:
    print('Operação - Adição!')

    try:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
    
    except ValueError:
        print("Erro: Digite apenas números válidos!")
        continue  

    soma = num1 + num2

    print(f'{num1} + {num2} = {soma}')

    while True:

        decisao = input('Deseja realizar mais uma soma? [S ou N]: ').strip().lower()
        
        if decisao == "n":
            print('Fechando programa...')
            exit()  
        elif decisao == "s":
            break  
        else:
            print('Entrada inválida! Digite apenas "S" ou "N".')
