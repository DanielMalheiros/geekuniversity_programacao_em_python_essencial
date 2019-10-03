"""35- Sejam A e B catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = raiz de (a ** 2 + b ** 2). Faça um programa que receba os valores de
A e B e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa operação."""

a = float(input("Insira o tamanho em centímetros de um dos catetos do triângulo: "))
b = float(input("Insira o tamanho em centímetros do outro cateto do triângulo: "))

hipotenusa = ((a ** 2) + (b ** 2) ** 1/2)
print(f"A hipotenusa terá {hipotenusa} centímetros.")
