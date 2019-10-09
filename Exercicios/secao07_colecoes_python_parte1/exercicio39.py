"""39- Escreva um programa que leia um número inteiro positivo n e em seguida imprima n
linhas do chamado Triangulo de Pascal:
ex:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
...
"""
lista = []
n = int(input("Insira um valor N:"))

if n > 0:
    lista = [[1], [1, 1]]
    for i in range(1, n):
        linha = [1]
        for j in range(0, len(lista[i]) - 1):
            linha += [lista[i][j] + lista[i][j + 1]]
        linha += [1]
        lista += [linha]

for linha in range(n+1):
    print(lista[linha])
