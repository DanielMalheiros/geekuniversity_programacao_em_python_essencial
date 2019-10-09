"""13- Gere uma matriz 4x4 com valores no intervalo [1, 20]. Escreva um programa que transforme a matriz
gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os elementos acima da diagonal principal.
Imprima a matriz original e a matriz transformada."""

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input(f"Defina um valor no intervalo [1, 20] para a posição [{i}][{j}] da matriz 4x4: "))
        while matriz[i][j] < 1 or matriz[i][j] > 20:
            matriz[i][j] = int(input(f"Valor inválido.\nDefina um valor no intervalo [1, 20] para a posição [{i}][{j}]"
                                     f" da matriz 4x4: "))
print("Matriz: ")
for i in range(4):
    for j in range(4):
        print(f"[{matriz[i][j]:^5}]", end=' ')
    print( )

for i in range(4):
    for j in range(4):
        if i == 0 and j >= 1:
            matriz[i][j] = 0
        elif i == 1 and j >= 2:
            matriz[i][j] = 0
        elif i == 2 and j == 3:
            matriz[i][j] = 0

print("Matriz transformada: ")
for i in range(4):
    for j in range(4):
        print(f"[{matriz[i][j]:^5}]", end=' ')
    print( )
