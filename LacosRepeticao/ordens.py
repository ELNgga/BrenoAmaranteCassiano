numero = []

while numero != "0":
    numeros = int(input("Digite o numero desejado:"))
    numero.append(numeros)

for i in range(numero):
    print(f"{i + 1} {numero[i]}")

    #ordem = input("Deseja que eles sejam informado em ordem crescente ou decrescente:")
    #if ordem == "crescente":
