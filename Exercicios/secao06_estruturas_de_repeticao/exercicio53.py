"""53- Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do
chamado triangulo de Floyd. Para n = 6, temos:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21"""

valor = int(input('Digite um valor: '))
z = 1
for i in range(valor+1):
    for f in range(i):
        print(z, end=' ')
        z += 1
    print('')