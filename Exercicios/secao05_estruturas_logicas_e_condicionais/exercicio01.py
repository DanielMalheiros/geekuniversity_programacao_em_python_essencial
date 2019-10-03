"""1- Faça um programa que receba dois números e mostre qual deles
é o maior."""

num1 = int(input("Escolha um número: "))
num2 = int(input("Escolha outro número: "))
if num1 > num2:
    print(f"O maior entre estes dois valores é o {num1}")
elif num2 > num1:
    print(f"O maior entre estes dois valores é o {num2}")
elif num1 == num2:
    print("Os valores são iguais.")