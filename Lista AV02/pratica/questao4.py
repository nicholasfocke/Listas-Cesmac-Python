def calcular(numero1, numero2, operacao):
    if operacao == 'somar':
        return numero1 + numero2
    
    elif operacao == 'subtrair':
        return numero1 - numero2
    
    elif operacao == 'multiplicar':
        return numero1 * numero2
    
    elif operacao == 'dividir':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: divisão por zero"
    else:
        return "Operação inválida"


print(calcular(5, 3, 'somar'))         
print(calcular(10, 4, 'subtrair'))    
print(calcular(2, 3, 'multiplicar'))  
print(calcular(10, 2, 'dividir'))      
print(calcular(10, 0, 'dividir')) 
