"""10- Faça um programa que receba a altura e sexo de uma pessoa e calcule e mostre
seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
a) Homens (72.7 * h) - 58
b) Mulheres (62.1 * h) - 44.7"""

altura = float(input("Qual sua altura? (ex. 1.71, 1.80...)"))
sexo = input("Qual seu sexo? (M/F)")

if sexo.lower() == 'm':
    print(f"Seu peso ideal é {(72.7 * altura) - 58:.2f} quilos.")
elif sexo.lower() == 'f':
    print(f"Seu peso ideal é {(62.1 * altura) - 44.7:.2f} quilos.")
else:
    print("Sexo inválido.")
