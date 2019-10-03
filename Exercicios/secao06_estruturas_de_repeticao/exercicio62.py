"""62- Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro, cinco, então
há 2+4+4+6+5 = 22 letras usadas no total. Fala um programa que conte quantas letras seriam
utilizadas se todos os números de 1 a 1000 fossem escritos em palavras."""

numeros = {0: 'zero', 1: 'um', 2: 'dois', 3: 'tres', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito',
           9: 'nove'}
soma = 0
for i in range(1, 1001):
    num = list(str(i))
    for n in num:
        soma += len(numeros[int(n)])

print(soma)