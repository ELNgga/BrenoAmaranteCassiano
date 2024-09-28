nome = input("Digite seu nome:")
nota = float(input("Digite sua nota:"))

if nota >= 90:
    print(f"\nOlá, {nome}, sua nota foi classificada como A!\n")
elif nota >= 80:
    print(f"\nOlá, {nome}, sua nota foi classificada como B!\n")
elif nota >= 70:
    print(f"\nOlá, {nome}, sua nota foi classificada como C!\n")
elif nota >= 60:
    print(f"\nOlá, {nome}, sua nota foi classificada como D!\n")
else:
    print(f"\nOlá, {nome}, sua nota foi classificada como F!\n")
