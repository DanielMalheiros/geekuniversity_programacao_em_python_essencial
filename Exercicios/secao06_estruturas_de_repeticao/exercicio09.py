"""9- Faça um programa que leia um número inteiro N e depois imprima os N primeiros
números naturais ímpares."""

num = int(input("Digite um número inteiro: "))
loop = 0

for n in range(1, 99999999):
    if n % 2 != 0:
        print(n)
        loop = loop + 1
        if loop >= num:
            break