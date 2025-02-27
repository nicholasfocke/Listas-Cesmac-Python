produtos = [
    {'nome': 'shampoo', 'preço': 20.00,},
    {'nome': 'condicionador', 'preço': 18.00, },
    {'nome': 'sabonete', 'preço': 5.00,},
    {'nome': 'pasta de dente', 'preço': 10.00,},
    {'nome': 'escova de dente','preço': 15.00,},
]

for produto in produtos:
    print(f"{produto['nome']} - R${produto['preço']:.2f}")