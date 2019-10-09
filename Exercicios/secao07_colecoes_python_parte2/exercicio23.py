#  23- Faça um programa que leia uma matriz A de tamanho 3x3 e calcule B = A ** 2.

a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        a[i][j] = int(input(f"Defina um valor para a posição [{i}][{j}] da matri 3 x 3 A: "))
        b[i][j] = a[i][j] ** 2

print("Matriz A:")
for i in range(3):
    for j in range(3):
        print(f"[{a[i][j]:^5}]", end=' ')
    print( )

print("Matriz B: ")
for i in range(3):
    for j in range(3):
        print(f"[{b[i][j]:^5}]", end=' ')
    print( )
