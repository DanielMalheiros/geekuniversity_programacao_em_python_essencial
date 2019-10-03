"""36- Escreva um programa que dado o valor da venda, imprima a comissão que deverá ser
paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:

VENDA MENSAL                                                                COMISSÃO
Maior ou igual a R$100.000,00                                       R$700,00 + 16% das vendas
Menor que R$100.000,00 e maior ou igual a R$80.000,00               R$650,00 + 14% das vendas
Menor que R$80.000,00 e maior ou igual a R$60.000,00                R$600.00 + 14% das vendas
Menor que R$60.000,00 e maior ou igual a R$40.000,00                R$550,00 + 14% das vendas
Menor que R$40.000,00 e maior ou igual a R$20.000,00                R$500,00 + 14% das vendas
Menor que R$20.000,00                                               R$400,00 + 14% das vendas
"""

venda = float(input("Que valor foi vendido? "))

if venda >= 100_000:
    comissao = 700 + (venda * 1.16)
elif 100_000 > venda >= 80_000:
    comissao = 650 + (venda * 1.14)
elif 80_000 > venda >= 60_000:
    comissao = 600 + (venda * 1.14)
elif 60_000 > venda >= 40_000:
    comissao = 550 + (venda * 1.14)
elif 40_000 > venda >= 20_000:
    comissao = 500 + (venda * 1.14)
else:
    comissao = 400 + (venda * 1.14)

print(f"Sua comissão será de R${comissao}")
