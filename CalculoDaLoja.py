usuario = input("Usuario:")
print(f"Olá {usuario}!\n")
vTotal = float(input("\nDigite o valor da sua compra:"))
formaPag = input("Digite sua forma de pagamento:")

desc10 = vTotal - (vTotal * 0.10)
desc15 = vTotal - (vTotal * 0.15)
desc20 = vTotal - (vTotal * 0.20)

if formaPag == "a vista":
    if vTotal <= 500:
        print(f"Valor Final:{desc10}")
    elif vTotal > 500:
        print(f"Valor Final:{desc15}")
    elif vTotal > 1000:
        print(f"Valor Final:{desc20}")
if formaPag == "a prazo":
    print("Consiguimos parcelar em até 18x, apartir de 10x sera adicionado juros a o valor!")
    parc = input(int("Digite a quantidade de parcelas:"))
    valorParc = vTotal / parc
    while vTotal <= 800 and parc >=5:
        print("Quantidade de parcelas maximas para o valor é 5!")
    if vTotal <= 800 and parc <=5:   
        print(f"{parc}x de R${valorParc}.")
    if vTotal > 800 and parc <= 10:
        print(f"{parc}x de R${valorParc}.")
          
