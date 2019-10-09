#  9- Leia uma matriz de 3x3 elementos. Calcule a soma dos elementos que estão abaixo da diagonal principal.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Defina um valor para a posição [{i}][{j}] da matriz 3x3."))

for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]", end=' ')
    print( )

soma = matriz[1][0] + matriz[2][0] + matriz[2][1]
print(f"A soma entre os valores abaixo da diagonal principal é de {soma}.")
