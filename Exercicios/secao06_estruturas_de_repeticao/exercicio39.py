"""39- Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas pelo usuário.
Esse programa não pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0."""

base = int(input("Insira a base do triangulo: "))
altura = int(input("Insira a altura do triangulo: "))

while base > 0 and altura > 0:
    area = (base * altura) / 2
    break

print(area)
