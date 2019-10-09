#  Leia uma matriz de 3x3 elementos. Calcule e imprima a sua transposta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriztransposta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Defina um valor para a posição [{i}][{j}] da matriz 3x3: "))

for i in range(3):
    for j in range(3):
        matriztransposta[i][j] = matriz[j][i]

print("Matriz: ")
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]", end=' ')
    print( )

print("Matriz Transposta: ")
for i in range(3):
    for j in range(3):
        print(f"[{matriztransposta[i][j]:^5}]", end=' ')
    print( )
