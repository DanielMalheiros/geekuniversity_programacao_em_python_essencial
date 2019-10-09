"""33- Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições
com valor zero. Para isso, todos os elementos à frente do valor zero devem ser movidos uma posição para
trás no vetor."""

contador = 0
vetor = []

while contador < 15:
    valor = int(input(f"Digite um valor para o vetor ({contador+1}/15): "))
    vetor.append(valor)
    contador += 1

print(vetor)

while 0 in vetor:
    vetor.pop(vetor.index(0))

print(vetor)
