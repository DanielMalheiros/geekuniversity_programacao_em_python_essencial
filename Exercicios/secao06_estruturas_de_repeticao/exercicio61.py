"""61- Faça um programa que calcule o maior número palíndromo feito a partir do produto de dois números
de 3 dígitos. Ex. O maior palíndromo feito a partir do produto de dois números de dois dígitos é
9009 = 91 * 99"""

i = 0
j = 0
pol = 0
while i <= 999:
    j = i
    while j <= 999:
        temp = str(i * j)
        tempInverso = temp[::-1]
        if temp == tempInverso:
            polTemp = int(temp)
            if polTemp > pol:
                pol = polTemp
        j += 1
    i += 1
print(pol)