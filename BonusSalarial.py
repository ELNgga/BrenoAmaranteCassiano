nome = input("Digite seu nome:")
sal = float(input("Digite seu salario atualmente em R$:"))
temp = float(input("Digite seu tempo de trabalho no seu atual emprego em anos:"))

bonus = sal * 0.05 + sal

if temp > 5:
    print(f"\nSeu salario recebeu um bonus de 5% portanto passa a ser R${bonus}!\n")
else:
    print("\nVoce ainda não tem o tempo necessario para o bonus salarial!\n")