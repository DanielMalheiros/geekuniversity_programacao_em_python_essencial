"""54- Faça um programa que receba um número inteiro maior do que 1 e
verifique se o número fornecido é número primo ou não."""

num = int(input("Digite um número inteiro positivo: "))
tot = 0

if num > 0:
    for c in range(1, num+1):
        if num % c == 0:
            tot += 1
    if tot == 2:
         print(f"O número {num} é primo.")
    else:
        print(f"O número {num} não primo.")
else:
    print("Número inválido.")