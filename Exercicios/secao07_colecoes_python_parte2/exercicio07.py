"""7- Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da forma:

A[i][j] = 2i + 7j - 2 se i < j
A[i][j] = 3i ** 2 - 1 se i = j
A[i][j] = 4i ** 3 - 5j ** 2 + 1 se i > j
"""

matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for linha in range(10):
    for coluna in range(10):
        if linha < coluna:
            matriz[linha][coluna] = 2 * linha + 7 * coluna
        elif linha == coluna:
            matriz[linha][coluna] = (3 * linha) ** 2 - 1
        else:
            matriz[linha][coluna] = (4 * linha) ** 3 - (5 * coluna) ** 2

for linha in range(10):
    for coluna in range(10):
        print(f"[{matriz[linha][coluna]:^5}]", end=' ')
    print( )
