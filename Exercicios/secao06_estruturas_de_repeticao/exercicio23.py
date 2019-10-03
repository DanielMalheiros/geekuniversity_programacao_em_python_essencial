"""23- Faça um algoritmo que leia um número positivo e imprima seus divisores."""

num = int(input("Insira um número positivo: "))

if num > 0:
    for n in range(1, num+1):
        if num % n == 0:
            print(n)
else:
    print("Número inválido.")
