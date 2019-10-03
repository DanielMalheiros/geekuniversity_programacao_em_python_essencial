"""25- Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5."""

soma = 0

for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        soma = soma + n

print(soma)