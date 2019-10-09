"""24-  Faça um programa para determinar a proxima jogada em um jogo da velha. Assumir que o tabuleiro é representado
por uma matriz de 3x3, onde cada posição representa uma das casas do tabuleiro. A matriz pode conter os seguintes
valores -1, 0, 1, representando respectivamente uma casa contendo uma peça minha (-1), uma casa vazia do tabuleiro (0),
e uma casa contendo uma peça de meu oponente (1)

Exemplo:
-1   1   1
-1  -1   0
0    1   0
"""
contador = 0

#  considerando o atual tabuleiro de jogo da velha:

matriz = [[-1, 0, 0], [0, 1, -1], [1, 0, -1]]

for i in range(3):
    for j in range(3):
        if j < 2:
            print(f"{matriz[i][j]:^3}", end='|')
        if j == 2:
            print(f"{matriz[i][j]:^3}",)
    if i < 2:
        print('-----------')

print("Jogadas disponiveis: ")
for i in range(3):
    for j in range(3):
        if matriz[i][j] == 0:
            print(f"Posição {contador + 1}: [{i}][{j}]")
        contador += 1

while True:
    jogada = int(input("Em qual posiçao disponivel você deseja realizar sua jogada?\n(1) (2) (3) (4):"))
    if jogada != 1 and jogada != 2 and jogada != 3 and jogada != 4:
        print("Posição invalida.")
        jogada = int(input("Em qual posiçao disponivel você deseja realizar sua jogada?\n(1) (2) (3) (4):"))
    if jogada == 1:
        matriz[0][1] = -1
        break
    if jogada == 2:
        matriz[0][2] = -1
        print("Parabens, você venceu!")
        break
    if jogada == 3:
        matriz[1][0] = -1
        break
    if jogada == 4:
        matriz[2][1] = -1
        break

for i in range(3):
    for j in range(3):
        if j < 2:
            print(f"{matriz[i][j]:^3}", end='|')
        if j == 2:
            print(f"{matriz[i][j]:^3}",)
    if i < 2:
        print('-----------')
