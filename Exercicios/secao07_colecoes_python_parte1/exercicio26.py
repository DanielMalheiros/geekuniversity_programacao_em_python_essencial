"""26- Faça um programa que calcule o desvio padrão de um vetor V contendo N = 10 números,
onde M é a media do valor."""

import math
v = []
contador = 0
soma = 0

while contador < 10:
    valor = int(input(f"Defina um valor para o vetor ({contador+1}/10)"))
    v.append(valor)
    contador += 1

media = sum(v) / len(v)
for n in v:
    soma += (n - media) ** 2
desviopadrao = math.sqrt(soma / len(v))
print(f"O desvio padrão é de {desviopadrao:.2f}.")
print(len(v))
