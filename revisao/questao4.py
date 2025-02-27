while True:
    print("Bem-vindo ao Conversor de Temperaturas!")
    print("Escolha uma opção:")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")
    
    opcao = input("Opção: ")

    if opcao == "1":
        celsius = float(input("\n Digite a temperatura em Celsius: "))

        fahrenheit = (celsius * 9/5) + 32

        print(f"{celsius} graus Celsius é igual a {fahrenheit:.1f} graus Fahrenheit.")

    elif opcao == "2":

        fahrenheit = float(input("\n Digite a temperatura em Fahrenheit: "))

        celsius = (fahrenheit - 32) * 5/9

        print(f"{fahrenheit} graus Fahrenheit é igual a {celsius:.1f} graus Celsius.")

    else:
        print("Opção inválida! Escolha 1 ou 2.")

    continuar = input("\nDeseja fazer outra conversão? (s/n): ").strip().lower()

    if continuar != "s":

        print("Encerrando o programa. Até mais!")
        break
