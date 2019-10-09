#  4- Leia uma matriz 4x4, imprima a matriz e retorne a localização (linha e coluna) do maior valor.

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
maior_linha = 0
maior_coluna = 0
maior_valor = -999

for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = int(input(f"Defina um valor para a posição [{linha}][{coluna}] da matriz 4x4: "))

for linha in range(4):
    for coluna in range(4):
        if matriz[linha][coluna] > maior_valor:
            maior_valor = matriz[linha][coluna]
            maior_linha = linha
            maior_coluna = coluna

for linha in range(4):
    for coluna in range(4):
        print(matriz[linha][coluna], end=' ')
    print( )

print(f"O maior valor da matriz 4x4 é {maior_valor}, que está na linha {maior_linha} e na coluna {maior_coluna}.")
