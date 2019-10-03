"""28- Faça um programa que leia três números inteiros positivos e efetue o cálculo
de uma das seguintes médias de acordo com um valor digitado pelo usuário:
1) Geométrica: (x * y * x) ** 1/3
2) Ponderada: (x + 2 * y + 3 * z) / 6
3) Harmônica: 1 / (1 / x + 1 / y + 1 / z)
4) Aritmética: (x + y + z) / 3
"""

x = int(input("Defina o primeiro valor inteiro e positivo (X): "))
y = int(input("Defina o segundo valor inteiro e positivo (Y): "))
z = int(input("Defina o terceiro valor inteiro e positivo (Z): "))

if x > 0 and y > 0 and z > 0:
    select = input("Escolha a média a ser calculada:\n1- Geométrica\n2- Ponderada\n3- Harmônica\n4- Aritmética")
    if select == '1':
        media = (x * y * z) ** 1/3
        print(f"A média geométrica entre estes valores será de {media}.")
    elif select == '2':
        media = (x + 2 * y + 3 * z) / 6
        print(f"A média ponderada entre estes valores será de {media}.")
    elif select == '3':
        media = 1 / (1 / x + 1 / y + 1 / z)
        print(f"A média harmônica entre estes valores será de {media}.")
    elif select == '4':
        media = (x + y + z) / 3
        print(f"A média aritmética entre estes valores será de {media}.")
    else:
        print("Número inválido.")
else:
    print("Um dos valores não é um número inteiro ou não é positivo.")
