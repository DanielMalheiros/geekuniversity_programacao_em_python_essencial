"""7- Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor,
o maior elemento e a posição que ele se encontra."""

indice = 0
vetor = []

while indice < 10:
    valor = int(input(f"Digite um valor para o vetor ({indice+1}/10)"))
    vetor.append(valor)
    indice += 1

print(f"O maior elemento da lista {vetor} é o {max(vetor)}, posicionado no indice {vetor.index(max(vetor))}.")
