"""30- Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção
entre os 2 vetores anteriores, ou seja, que contém apenas os números que estão em ambos os vetores.
Não deve conter números repetidos."""

contador = 0
vetor1 = []
vetor2 = []

while contador < 10:
    valor = int(input(f"Digite um valor para o primeiro vetor ({contador+1}/10): "))
    vetor1.append(valor)
    contador += 1

contador = 0

while contador < 10:
    valor = int(input(f"Digite um valor para o segundo vetor ({contador+1}/10): "))
    vetor2.append(valor)
    contador += 1

set1 = set(vetor1)
set2 = set(vetor2)
print(f"Valores em comum entre os dois vetores: {set1.intersection(set2)}")
