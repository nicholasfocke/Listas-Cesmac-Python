def calcular_media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

print(calcular_media([10, 20, 30])) 