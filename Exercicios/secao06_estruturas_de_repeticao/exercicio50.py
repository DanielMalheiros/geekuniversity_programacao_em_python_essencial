"""50- Chico tem 1.50 metros e cresce 2cm por ano, enquanto Zé tem 1.10 metros e cresce 3 centímetros por
ano. Escreva um programa que calcule e imprima quantos anos serão necessarios para que Zé seja maior
que Chico."""

altura_chico = 1.5
altura_ze = 1.1
contador = 0

while altura_ze < altura_chico:
    altura_chico += 0.02
    altura_ze += 0.03
    contador += 1

print(contador)