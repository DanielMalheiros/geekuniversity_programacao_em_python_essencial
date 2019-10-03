"""12- Faça um algoritmo que leia um número inteiro. Se o número for negativo, escreva
a mensagem "Número inválido. Se positivo, calcular o logaritmo deste número."""

import math

num = int(input("Escolha um número: "))

if num < 0:
    print("Número inválido.")
else:
    print(f"O log de {num} é {math.log10(num)}.")
