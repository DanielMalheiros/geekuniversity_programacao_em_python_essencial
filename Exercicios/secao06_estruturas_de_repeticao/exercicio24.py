"""24- Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores
desse número, com exceção dele proprio. Ex: A soma dos divisores do número 66 é:
1+2+3+6+11+22+33 = 78."""

num = int(input("Insira um número positivo: "))
soma = 0

if num > 0:
    for n in range(1, num):
        if num % n == 0:
            soma = soma + n
else:
    print("Número inválido.")

print(f"A soma dos divisores de {num} é {soma}.")