"""14- Faça um programa para gerar automaticamente números entre 0 e 99 de uma cartela
de bingo. Sabendo que cada cartela deverá conter 5 linhas de 5 números, gere esses dados
de modo a não ter números repetidos dentro das cartelas. O programa deve exibir na tela a
cartela gerada."""

import random
num = []
matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i in range(5):
    for j in range(5):
        matriz[i][j] = random.randint(0, 99)
        num.append(matriz[i][j])
        while num in matriz:
            matriz[i][j] = random.randint(0, 99)

for i in range(5):
    for j in range(5):
        print(f"[{matriz[i][j]:^5}]", end=' ')
    print( )