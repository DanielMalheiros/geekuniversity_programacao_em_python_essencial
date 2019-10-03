"""8- Escreva um programa que leia 10 números e escreva o menor valor lido e o maior
valor lido."""

maior_valor = -99999
menor_valor = 99999

for n in range(10):
    valor = int(input(f"Insira um valor {n+1}/10: "))
    if valor > maior_valor:
        maior_valor = valor
    elif valor < menor_valor:
        menor_valor = valor

print(f"O menor valor é {menor_valor} e o maior valor é {maior_valor}")