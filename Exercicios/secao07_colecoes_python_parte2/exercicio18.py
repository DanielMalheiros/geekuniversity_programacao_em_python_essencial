"""18 - Faça um programa que permita ao usuário entrar com uma matriz de 3x3 números inteiros. Em seguida, gere um array
unidimensional pela soma dos números de cada coluna da matriz e mostrar na tela esse array."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
vetor = []
soma = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite um valor para a posição [{i}][{j}] da matriz 3 x 3: "))

for i in range(3):
    soma += matriz[i][0]
vetor.append(soma)
soma = 0

for i in range(3):
    soma += matriz[i][1]
vetor.append(soma)
soma = 0

for i in range(3):
    soma += matriz[i][2]
vetor.append(soma)

for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]", end=' ')
    print( )
print(vetor)
