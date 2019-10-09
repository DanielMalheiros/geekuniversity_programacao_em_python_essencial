#  6- Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada posição das matrizes lidas.

matriz_1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz_2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz_3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for linha in range(4):
    for coluna in range(4):
        matriz_1[linha][coluna] = int(input(f"Digite um valor para a posição [{linha}][{coluna}] da matriz 1: "))
        matriz_2[linha][coluna] = int(input(f"Digite um valor para a posição [{linha}][{coluna}] da matriz 2: "))

for linha in range(4):
    for coluna in range(4):
        if matriz_1[linha][coluna] >= matriz_2[linha][coluna]:
            matriz_3[linha][coluna] = matriz_1[linha][coluna]
        elif matriz_1[linha][coluna] < matriz_2[linha][coluna]:
            matriz_3[linha][coluna] = matriz_2[linha][coluna]

print("Matriz 1: ")
for linha in range(4):
    for coluna in range(4):
        print(matriz_1[linha][coluna], end=' ')
    print( )

print("Matriz 2: ")
for linha in range(4):
    for coluna in range(4):
        print(matriz_2[linha][coluna], end=' ')
    print( )

print("Matriz 3: ")
for linha in range(4):
    for coluna in range(4):
        print(matriz_3[linha][coluna], end=' ')
    print( )