"""40- O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do
distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de
fabrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo para
o consumidor
CUSTO DE FÁBRICA                        % DISTRIBUIDOR                % DOS IMPOSTOS
até R$12.000,00                               5                            ISENTO
até R$ 12.000,00 e 25.000,00                 10                              15
acima de R$25.000,00                         15                              20
"""

custo_fab = float(input("Qual o custo de fábrica do carro que você deseja comprar? "))

if custo_fab < 12_000:
    print(f"O preço será de R${custo_fab * 1.05}")
elif custo_fab >= 12_000 and custo_fab <= 25_000:
    print(f"O preço será de R${custo_fab * 1.25}")
elif custo_fab > 25_000:
    print(f"O preço será de R${custo_fab * 1.35}")
