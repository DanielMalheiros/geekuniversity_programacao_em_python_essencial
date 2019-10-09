"""21- Faça um programa que leia duas matrizes 2x2 com valores reais. Ofereça ao usuário um menu de opções:
a) Somar as duas matrizes;
b) Subtrair a primeira matriz da segunda;
c) Adicionar uma constante as duas matrizes;
d) Imprimir as matrizes

Nas duas primeiras opções uma terceira matriz 3 x 3 deve ser criada. Na terceira opção o valor da constante deve ser
lido e o resultado da adição da constante deve ser armazenado na propria matriz.
"""

matriz1 = [[0, 0], [0, 0]]
matriz2 = [[0, 0], [0, 0]]
matriz3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(2):
    for j in range(2):
        matriz1[i][j] = float(input(f"Defina um valor para a posição [{i}][{j}] da matriz 1: "))
        matriz2[i][j] = float(input(f"Defina um valor para a posição [{i}][{j}] da matriz 2: "))

menu = input("Selecione uma opção abaixo:\na)Somar as duas matrizes\nb)Subtrair a primeira matriz da segunda\n"
             "c)Adicionar uma constante as duas matrizes\nd)Imprimir as matrizes")
while menu != 0:
    if menu == 'a':
        print("Somar as duas matrizes selecionado. ")
        for i in range(2):
            for j in range(2):
                matriz3[i][j] = matriz1[i][j] + matriz2[i][j]
        menu = input("Selecione uma opção abaixo:\na)Somar as duas matrizes\nb)Subtrair a primeira matriz da segunda\n"
                     "c)Adicionar uma constante as duas matrizes\nd)Imprimir as matrizes")
    elif menu == 'b':
        print("Subtrair as duas matrizes selecionado. ")
        for i in range(2):
            for j in range(2):
                matriz3[i][j] = matriz1[i][j] - matriz2[i][j]
        menu = input("Selecione uma opção abaixo:\na)Somar as duas matrizes\nb)Subtrair a primeira matriz da segunda\n"
                     "c)Adicionar uma constante as duas matrizes\nd)Imprimir as matrizes")
    #  elif menu == 'c':
    elif menu == 'd':
        print("MATRIZ 1")
        for i in range(2):
            for j in range(2):
                print(f"[{matriz1[i][j]:^5}]", end='')
            print( )
        print("MATRIZ 2")
        for i in range(2):
            for j in range(2):
                print(f"[{matriz2[i][j]:^5}]", end='')
            print( )
        print("MATRIZ 3")
        for i in range(3):
            for j in range(3):
                print(f"[{matriz3[i][j]:^5}]", end='')
            print( )
        menu = input("Selecione uma opção abaixo:\na)Somar as duas matrizes\nb)Subtrair a primeira matriz da segunda\n"
                     "c)Adicionar uma constante as duas matrizes\nd)Imprimir as matrizes")
    if menu == '0':
        break
