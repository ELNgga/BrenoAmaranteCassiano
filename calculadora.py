nome = input("Digite seu nome:")
num1 = float(input("Digite um numero para a operação:"))
num2 = float(input("Digite outro numero para sua operação:"))
ope = input("Digite o simbolo da sua operação:")

resAdi = num1 + num2
resSub = num1 - num2
resDiv = num1 / num2
    if num2 == 0:
        print("Não é possivel dividir por zero!")
resMult = num1 * num2

if ope == "+":
    print(f"\nOlá {nome}, o resultado da sua operação é: {resAdi}!")
elif ope == "-":
    print(f"\nOlá {nome}, o resultado da sua operação é: {resSub}!")
elif ope == "/": 
        print(f"\nOlá {nome}, o resultado da sua operação é: {resDiv}!")
elif ope == "*":
    print(f"\nOlá {nome}, o resultado da sua operação é: {resMult}!")