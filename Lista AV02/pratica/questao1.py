def verifica_sinal(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

print(verifica_sinal(10))  
print(verifica_sinal(-3))   
print(verifica_sinal(0))    
