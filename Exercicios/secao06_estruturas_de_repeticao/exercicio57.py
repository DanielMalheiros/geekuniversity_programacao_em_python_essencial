"""57- Faça um programa que conte quantos números primos existem entre a e b, onde a e b são números informados
pelo usuário."""

num1 = int(input("Insira o primeiro número:"))
num2 = int(input("Insira o segundo número:"))
tot = 0
print(f"Os números primos no intervalo entre {num1} e {num2} são:")
contador = 0

if num1 > 0 and num2 > 0 and num2 > num1:
    for numero in range(num1, num2+1):
        for n in range(1, numero+1):
            if numero % n == 0:
                tot += 1
        if tot == 2:
            print(numero,end=' ')
            contador += 1
        tot = 0
print(f"({contador} números primos)")