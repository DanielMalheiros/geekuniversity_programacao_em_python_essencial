"""58- Faça um programa que some os números primos existentes entre a e b, onde a e b são números informados
pelo usuário."""

num1 = int(input("Insira o primeiro número:"))
num2 = int(input("Insira o segundo número:"))
tot = 0
soma = 0

if num1 > 0 and num2 > 0 and num2 > num1:
    for numero in range(num1, num2+1):
        for n in range(1, numero+1):
            if numero % n == 0:
                tot += 1
        if tot == 2:
            print(numero)
            soma += numero
        tot = 0
print(f"A soma entre os números primos no intervalo de {num1} a {num2} é {soma}.")