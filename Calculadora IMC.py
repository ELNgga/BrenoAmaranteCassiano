nome = input("Olá, Digite seu nome:")
peso = float(input("Digite seu peso em KG:"))
alt = float(input("Digite sua altura em Metros:"))

imc = peso / alt ** 2

print(f"Boa Dr. {nome}")
print(f"Seu IMC é {imc:.2f} !")