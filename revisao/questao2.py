
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"\nMédia: {media:.2f}")

if media >= 7:
    print("Aprovado!")
elif 4 <= media < 7:
    print("Reposição!")
else:
    print("Reprovado!")
