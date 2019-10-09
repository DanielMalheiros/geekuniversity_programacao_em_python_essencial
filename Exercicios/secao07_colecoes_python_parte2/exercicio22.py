#  22- Faça um programa que leia duas matrizes A e B de tamanho 3x3 e calcule C = A * B;

a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        a[i][j] = int(input(f"Defina um valor para a posição [{i}][{j}] da matriz A: "))
        b[i][j] = int(input(f"Defina um valor para a posição [{i}][{j}] da matriz B: "))
        c[i][j] = a[i][j] * b[i][j]

print("Matriz A:")

for i in range(3):
    for j in range(3):
        print(f"[{a[i][j]:^5}]", end='')
    print( )

print("Matriz B:")

for i in range(3):
    for j in range(3):
        print(f"[{b[i][j]:^5}]", end='')
    print( )

print("Matriz C:")

for i in range(3):
    for j in range(3):
        print(f"[{c[i][j]:^5}]", end='')
    print( )
