"""31- Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela
a seguir, verifique e mostre qual a classificação dessa pessoa.
ALTURA                            PESO
                      Até 60   de 60 a 90    90+
Menor que 1,20          A          D          G
De 1,20 a 1,70          B          E          H
Maior que 1,70          C          F          I
"""

altura = float(input("Insira sua altura: "))
peso = float(input("Insira seu peso: "))

if altura < 1.20:
    if peso < 60:
        print("Classificação A")
    elif peso >= 60 and peso <= 90:
        print("Classificação D")
    else:
        print("Classificação G")
elif altura >= 1.20 and altura <= 1.70:
    if peso < 60:
        print("Classificação B")
    elif peso >= 60 and peso <= 90:
        print("Classificação E")
    else:
        print("Classificação H")
elif altura > 1.70:
    if peso < 60:
        print("Classificação C")
    elif peso >= 60 and peso <= 90:
        print("Classificação F")
    else:
        print("Classificação I")
