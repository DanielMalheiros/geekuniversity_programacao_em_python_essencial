"""16- Usando switch escreva um programa que leia um inteiro entre 1 e 12 e
imprima o mês correspondente a este número. Isto é, janeiro se 1, fevereiro
se 2, e assim por diante."""

num = int(input("Escolha um número: "))

if num == 1:
    print("Janeiro")
elif num == 2:
    print("Fevereiro")
elif num == 3:
    print("Março")
elif num == 4:
    print("Abril")
elif num == 5:
    print("Maio")
elif num == 6:
    print("Junho")
elif num == 7:
    print("Julho")
elif num == 8:
    print("Agosto")
elif num == 9:
    print("Setembro")
elif num == 10:
    print("Outubro")
elif num == 11:
    print("Novembro")
elif num == 12:
    print("Dezembro")
else:
    print("Número inválido.")
