"""43- Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
a) o total a pagar com desconto de 10%
b) o valor de cada parcela, no parcelamento de 3x sem juros
c) a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
d) a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""

valor = float(input("Qual o valor da compra? "))
print(f"Total a pagar com desconto de 10%: R${valor * 0.9}")
print(f"Valor de cada parcela, no parcelamento 3x sem juros: R${valor / 3:.2f}")
print(f"Comissão do vendedor (venda a vista): R${(valor * 0.9) * 0.05}")
