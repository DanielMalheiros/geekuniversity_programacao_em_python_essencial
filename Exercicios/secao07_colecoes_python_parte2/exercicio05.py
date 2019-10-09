"""5- Leia uma matriz 5x5. Leia tambem um valor X. O programa deverá fazer uma busca desse
valor na matriz e, ao final, escrever a localização (linha e coluna) ou uma mensagem de
"não encontrado"."""

matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
contador = 0

for linha in range(5):
    for coluna in range(5):
        matriz[linha][coluna] = int(input(f"Digite um valor para a posição [{linha}][{coluna}] da matriz:"))

x = int(input("Digite um valor para ser procurado na matriz: "))

for linha in range(5):
    for coluna in range(5):
        if matriz[linha][coluna] == x:
            print(f"O valor {x} se encontra na posição [{linha}][{coluna}] na matriz.")
        elif matriz[linha][coluna] != x:
            contador += 1
if contador == 25:
    print("Não encontrado.")
