"""33- Um produto vai sofrer aumento de preço de acordo com a tabela abaixo. Leia o
preço e calcule e escreva o preço novo, e escreva uma mensagem em função do preço
novo de acordo com a segunda tabela.
PREÇO ANTIGO                  PERCENTUAL DE AUMENTO
até R$50                               5%
entre R$50 e R$100                    10%
acima de R$100                        15%

PREÇO NOVO                    MENSAGEM
até R$80                       BARATO
entre R$80 e R$120             NORMAL
entre R$120 e R$200             CARO
acima de R$200               MUITO CARO
"""

preco = float(input("Qual o preço do produto em reais? "))

if preco < 50:
    novo_preco = preco * 1.05
elif preco >= 50 and preco <= 100:
    novo_preco = preco * 1.10
elif preco > 100:
    novo_preco = preco * 1.15

if novo_preco < 80:
    print(f"Com o aumento, o novo preço será de R${novo_preco:.2f}.")
    print("Barato.")
elif novo_preco >= 80 and novo_preco <= 120:
    print(f"Com o aumento, o novo preço será de R${novo_preco:.2f}.")
    print("Normal.")
elif novo_preco > 120 and novo_preco <=200:
    print(f"Com o aumento, o novo preço será de R${novo_preco:.2f}.")
    print("Caro.")
elif novo_preco > 200:
    print(f"Com o aumento, o novo preço será de R${novo_preco:.2f}.")
    print("Muito caro.")
