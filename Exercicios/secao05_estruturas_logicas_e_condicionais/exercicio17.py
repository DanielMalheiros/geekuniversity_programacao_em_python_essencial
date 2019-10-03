"""17- Faça um programa que calcule e mostre a área de um trapezio.
Sabe-se que: Area = ([base maior + base menor]) * altura / 2
Lembre-se que as bases devem ser números maiores que zero."""

base_maior = float(input("Qual o tamanho da base maior (em centímetros)?"))
base_menor = float(input("Qual o tamanho da base menor (em centímetros)?"))
altura = float(input("Qual a altura do trazepio (em centímetros)?"))

if base_maior > 0 and base_menor > 0 and altura > 0:
    area = ((base_maior + base_menor) * altura) / 2
    print(f"A area do trapézio é de {area} centímetros quadrados.")
else:
    print("Valor(es) inválido(s).")