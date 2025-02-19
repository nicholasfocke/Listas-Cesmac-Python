turno = input('Digite o turno em que você estuda [M]atutino, [V]espertino, [N]oturno: ').lower()

if turno == "m":
    print("BOM DIA!")

elif turno == "v":
    print("BOA TARDE!")

elif turno == "n":
    print("BOA NOITE!")

else:
    print("Valor inválido!")