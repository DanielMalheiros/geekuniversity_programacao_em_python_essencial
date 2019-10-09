"""Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso
o maior e o menor elemento do vetor."""

indice = 0
vetor = []

while indice < 10:
    valor = int(input(f"Digite um valor para o vetor ({indice+1}/10): "))
    vetor.append(valor)
    indice += 1

print(f"O maior elemento no vetor {vetor} é {max(vetor)}.")
print(f"O menor elemento no vetor {vetor} é {min(vetor)}.")
