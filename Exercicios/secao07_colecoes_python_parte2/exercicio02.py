"""2- Declare uma matriz 5x5. Preencha com 1 a diagonal principal e com 0 os demais
elementos. Escreva ao final a matriz obtida."""

matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


for n in range(5):
    matriz[n][n] = 1

for linha in range(5):
    print(matriz[linha])
