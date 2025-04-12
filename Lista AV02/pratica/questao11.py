def converter_temperatura(valor, unidade_origem):
    if unidade_origem.lower() == "c":
        return (valor * 9/5) + 32  # Celsius para Fahrenheit
    elif unidade_origem.lower() == "f":
        return (valor - 32) * 5/9  # Fahrenheit para Celsius
    else:
        return "Unidade inválida (use 'C' ou 'F')"
    


print(converter_temperatura(28, "c"))              
print(converter_temperatura(80, "f"))
