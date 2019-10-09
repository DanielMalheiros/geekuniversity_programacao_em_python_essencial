#  8- Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão acima da diagonal principal.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Digite um valor para a posição [{linha}][{coluna}]: "))

for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^5}]", end=' ')
    print( )

soma = matriz[0][1] + matriz[0][2] + matriz[1][2]
print(f"A soma entre os valores acima da diagonal principal é {soma}.")
