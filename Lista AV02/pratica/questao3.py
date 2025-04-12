def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

print(somar(5, 3))         
print(subtrair(10, 4))    
print(multiplicar(2, 3))   
print(dividir(10, 2))      
print(dividir(10, 0))     