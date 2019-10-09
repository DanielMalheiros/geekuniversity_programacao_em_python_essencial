"""13- Faça um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o
maior e o menor valor."""

indice = 0
vetor = []

while indice < 5:
    valor = int(input(f"Digite um valor para o vetor ({indice+1}/5): "))
    vetor.append(valor)
    indice += 1

print(f"O maior valor se encontra no indice {vetor.index(max(vetor))} ({max(vetor)}) e o menor no "
      f" {vetor.index(min(vetor))} ({min(vetor)})")
