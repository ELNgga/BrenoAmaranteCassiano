lista = []
contador = 0
soma = 0

while contador <= 4:
    numero = float(input("Digite um numero:"))
    lista.append(numero)

    contador += 1
    soma += numero

print(f"{soma}")