"""6- Faça um programa que leia 10 inteiros e imprima sua média."""

soma = 0

for n in range(10):
    valor = int(input(f"Insira um valor ({n+1}/10):"))
    soma = soma + valor

print(f"A média entre estes valores é {soma/10}")