"""4- Faça um programa que leia um vetor de 8 posições e, seguida, leia tambem dois valores
X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa deverá escrever
a soma dos valores encontrados nas respectivas posições X e Y."""

indice = 0
lista = []

while indice < 8:
    valor = int(input(f"Digite um valor para o vetor ({indice+1}/8): "))
    lista.append(valor)
    indice += 1

x = int(input(f"Escolha uma das posições do vetor para a soma (de 0 à 7):\n{lista}"))
y = int(input(f"Escolha uma outra posição do vetor para a soma (de 0 à 7):\n{lista}"))

if 0 < x < 8 and 0 < y < 8:
    soma = lista[x] + lista[y]
    print(f"A soma entre o valor {lista[x]} (indice {x}) e {lista[y]} (indice {y}) é de {soma}.")
else:
    x = int(input("Escolha uma das posições do vetor para a soma (de 0 à 7): "))
    y = int(input("Escolha uma outra posição do vetor para a soma (de 0 à 7) "))
