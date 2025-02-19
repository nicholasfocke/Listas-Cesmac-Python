vogais = ['a', 'e', 'i', 'o', 'u']

letra = input('Digite uma letra para saber se é vogal ou consoante: ').lower()

if letra in vogais:
    print(f'A letra "{letra}" é uma VOGAL!')

else:
    print(f'A letra "{letra}" é uma CONSOANTE!')