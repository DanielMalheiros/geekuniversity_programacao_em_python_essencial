"""20- Faça um programa que leia uma matriz 3x6 com valores reais.
a) Imprima a soma de todos os elementos das colunas ímpares.
b) Imprima a média aritmética dos elementos da segunda e quarta coluna.
c) Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2.
d) Imprima a matriz modificada.
"""

matriz = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
somaimpar = 0
soma = 0
divisor = 0

for i in range(3):
    for j in range(6):
        matriz[i][j] = int(input(f"Defina um valor para a posição [{i}][{j}] da matriz 3 x 6: "))

print("Coluna 0\tColuna 1\tColuna 2\tColuna 3\tColuna 4\tColuna 5:")
for i in range(3):
    for j in range(6):
        print(f"[{matriz[i][j]:^10}]", end='')
    print( )

for i in range(3):
    for j in range(6):
        if j % 2 != 0:
            somaimpar += matriz[i][j]
        if j == 1 or j == 3:
            soma += matriz[i][j]
            divisor += 1
        if j == 5:
            matriz[i][j] = matriz[i][0] + matriz[i][1]

mediaaritmetica = soma / divisor

print(f"Soma de todos os elementos nas colunas impares: {somaimpar}\nMédia aritmética dos elementos da segunda e"
      f" quarta coluna: {mediaaritmetica}\nMatriz modificada: ")

print("Coluna 0\tColuna 1\tColuna 2\tColuna 3\tColuna 4\tColuna 5:")
for i in range(3):
    for j in range(6):
        print(f"[{matriz[i][j]:^10}]", end='')
    print( )
