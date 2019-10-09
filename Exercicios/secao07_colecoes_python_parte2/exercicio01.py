#  1- Leia uma matriz 4x4, conte e escreva quantos valores maiores que 10 ela possui.

contador = 0
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
maiorque10 = []

for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = int(input(f"Defina um valor para a posição [{linha}][{coluna}] da matriz 4x4: "))
        if matriz[linha][coluna] > 10:
            maiorque10.append(matriz[linha][coluna])


for linha in range(4):
    for coluna in range(4):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print( )

if len(maiorque10) > 0:
    print(f"Existe(m) {len(maiorque10)} valor(es) maior(es) que 10 na matriz, ele(s) é/são:\n{maiorque10}")
else:
    print("Não existem valores maiores que 10 na matriz 4x4.")
