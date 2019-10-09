#  11- Leia uma matriz de 3x3 elementos. Calcule a soma dos elementos que estão na diagonal secundária.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Defina um valor para o elemento de posição [{i}][{j}] do vetor: "))

soma = matriz[0][2] + matriz[1][1] + matriz[2][0]

for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]", end=' ')
    print( )
print(f"A soma dos elementos na diagonal secundária é de {soma}.")
