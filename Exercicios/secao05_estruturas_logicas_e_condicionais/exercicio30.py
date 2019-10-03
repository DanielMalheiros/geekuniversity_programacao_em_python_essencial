"""30 - Faça um programa que receba três números e mostre-os em ordem crescente."""

num1 = int(input("Defina o primeiro número: "))
num2 = int(input("Defina o segundo número: "))
num3 = int(input("Defina o terceiro número: "))

maior = -999999
menor = 999999
do_meio = 0

if num1 != num2 and num2 != num3 and num1 != num3:
    if num1 > maior:
        maior = num1

    if num2 > maior:
        maior = num2

    if num3 > maior:
        maior = num3

    if num1 < menor:
        menor = num1

    if num2 < menor:
        menor = num2

    if num3 < menor:
        menor = num3

    if num1 < maior and num1 > menor:
        do_meio = num1

    if num2 < maior and num2 > menor:
        do_meio = num2

    if num3 < maior and num3 > menor:
        do_meio = num3

    print(f"{menor} < {do_meio} < {maior}")

elif num1 == num2:
    if num1 > num3:
        print(f"{num3} < {num2} = {num1}")
    elif num3 > num1:
        print(f"{num1} = {num2} < {num3}")

elif num1 == num3:
    if num1 > num2:
        print(f"{num2} < {num1} = {num3}")
    elif num1 < num2:
        print(f"{num1} = {num3} < {num2}")

elif num2 == num3:
    if num1 > num2:
        print(f"{num2} = {num3} < {num1}")
    elif num1 < num2:
        print(f"{num1} < {num2} = {num3}")

if num1 == num2 and num2 == num3 and num3 == num1:
    print(f"{num1} = {num2} = {num3}")
