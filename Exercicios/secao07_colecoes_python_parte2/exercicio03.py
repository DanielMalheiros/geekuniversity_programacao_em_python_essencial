"""3- Faça um programa que preenche uma matriz 4 x 4 com o produto do valor da linha e da coluna
de cada elemento. Em seguida, imprima na tela a matriz."""

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = linha * coluna

for linha in range(4):
    for coluna in range(4):
        print(matriz[linha][coluna], end=' ')
    print( )
