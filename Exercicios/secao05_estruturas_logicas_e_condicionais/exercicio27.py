"""27- Escreva um programa que, dada a idade de um nadador, classifique-o em uma
das seguintes categorias:
Categoria     Idade
Infantil A    5 a 7
Infantil B    8 a 10
Juvenil A     11 a 13
Juvenil B     14 a 17
Sênior        maiores de 18 anos
"""

idade = int(input("Qual a idade do nadador?"))

if idade < 5:
    print("Idade inválida ou insuficiente para participar (a partir de 5 anos).")
elif idade >= 5 and idade < 8:
    print("Categoria Infantil A")
elif idade >=8 and idade < 11:
    print("Categoria Infantil B")
elif idade >= 11 and idade < 14:
    print("Categoria Juvenil A")
elif idade >= 14 and idade < 18:
    print("Categoria Juvenil B")
else:
    print("Categoria Sênior")
