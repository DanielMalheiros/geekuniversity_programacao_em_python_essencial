"""52- Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao
valor que cada deu para realização da aposta. Faça um programa que leia quanto cada apostador investiu,
o valor do prêmio, e imprima quanto cada um ganharia do prêmio base no valor investido."""

premio = float(input("Qual o valor do premio? "))
aposta1 = float(input("Quanto o primeiro amigo apostou? "))
aposta2 = float(input("Quanto o segundo amigo apostou? "))
aposta3 = float(input("Quanto o terceiro amigo apostou? "))
aposta_total = aposta1 + aposta2 + aposta3
porcentagem1 = (aposta1 / aposta_total) * 100
porcentagem2 = (aposta2 / aposta_total) * 100
porcentagem3 = (aposta3 / aposta_total) * 100

print(f"O primeiro amigo ganhará R${premio * (porcentagem1 / 100):.2f}")
print(f"O segundo amigo ganhará R${premio * (porcentagem2 / 100):.2f}")
print(f"O terceiro amigo ganhará R${premio * (porcentagem3 / 100):.2f}")
