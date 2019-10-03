"""15- Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima
o dia da semana correspondente a este número. Isto , domingo se 1, segunda se 2,
e assim por diante."""

num = int(input("Escolha um número de 1 a 7: "))

if num == 1:
    print("Domingo")
elif num == 2:
    print("Segunda")
elif num == 3:
    print("Terça")
elif num == 4:
    print("Quarta")
elif num == 5:
    print("Quinta")
elif num == 6:
    print("Sexta")
elif num == 7:
    print("Sabado")
else:
    print("Número inválido.")
