"""1- Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
maiores que 0."""

multiplo = 0

for n in range(1, 100):
    if n % 3 == 0:
        print(n)
        multiplo = multiplo + 1
        if multiplo == 5:
            break