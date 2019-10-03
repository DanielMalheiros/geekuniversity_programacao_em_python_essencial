"""5- Faça um programa que peça ao usúario para digitar 10 valores e some-os."""

soma = 0

for n in range(10):
    valor = int(input(f"Insira um valor ({n+1}/10):"))
    soma = soma + valor

print(f"A soma é destes valores é {soma}.")