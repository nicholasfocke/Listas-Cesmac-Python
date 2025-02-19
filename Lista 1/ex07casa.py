contador = 0

perguntas = [
    "Telefonou para a vítima? (sim/não): ",
    "Esteve no local do crime? (sim/não): ",
    "Mora perto da vítima? (sim/não): ",
    "Devia para a vítima? (sim/não): ",
    "Já trabalhou com a vítima? (sim/não): "
]

for pergunta in perguntas:
    resposta = input(pergunta).strip().lower()
    if resposta == "sim":
        contador += 1

if contador == 2:
    print("Suspeita")
elif 3 <= contador <= 4:
    print("Cúmplice")
elif contador == 5:
    print("Assassino")
else:
    print("Inocente")
