reservas = []
nomes = []
continua = "sim"
print("Bem vindo ao seu assistente de agendamento de voo!!\n")
print("*" * 30)
while continua == "sim":
    nome = input("\nDigite o nome do passageiro:")
    nomes.append(nome)

    reserva = input("Digite seu destino:")
    reservas.append(reserva)

    continua = input("Deseja informar mais algum? (sim/nao):")

for i in range(len(nomes)):
    print(f"{i + 1} {nomes[i]} - {reservas[i]}")