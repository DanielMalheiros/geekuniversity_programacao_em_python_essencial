#  10- Leia uma matriz de 3x3 elementos. Calcule a soma dos elementos que estão na diagonal principal.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i}][{j}]: "))

for i in range(3):
    soma += matriz[i][i]
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]", end=' ')
    print( )
print(f"A soma dos valores na diagonal a matriz é {soma}.")
