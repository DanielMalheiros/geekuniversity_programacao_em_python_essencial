"""36- Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100
números naturais e o quadrado da soma. Ex. A soma dos quadrados dos dez primeiros números
naturais é:
1 ** 2 + 2 ** 2 + 3 ** 2+...+10 ** 2 = 385
O quadrado da soma dos dez primeiros números naturais é:
(1+2+3+...+10) ** 2 = 3025
A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma
é 3025 - 385 = 2640."""

soma_dos_quadrados = 0
soma = 0

for n in range(101):
    soma_dos_quadrados = soma_dos_quadrados + (n ** 2)

for i in range(101):
    soma = soma + i

quadrado_da_soma = soma ** 2

diferenca = quadrado_da_soma - soma_dos_quadrados
print(f"Soma entre os quadrados: {soma_dos_quadrados}")
print(f"Quadrado da soma: {quadrado_da_soma}")
print(f"Diferença entre o quadrado da soma e a soma dos quadrados: {diferenca}")