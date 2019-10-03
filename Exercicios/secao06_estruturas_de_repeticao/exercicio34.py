"""34- Faça um programa que calcule o menor número divisível por cada um dos números de 1
a 20. Exemplo: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10
sem sobrar resto."""

cont = 1

while True:           #  certamente há um jeito mais inteligente de resolver exercicio...
    cont += 1
    if cont % 1 == 0 and cont % 2 == 0 and cont % 3 == 0 and cont % 4 == 0 and cont % 5 == 0 and cont % 6 == 0\
        and cont % 7 == 0 and cont % 8 == 0 and cont % 9 == 0 and cont % 10 == 0 and cont % 11 == 0 and cont % 12 == 0\
        and cont % 13 == 0 and cont % 14 == 0 and cont % 15 == 0 and cont % 16 == 0 and cont % 17 == 0\
        and cont % 18 == 0 and cont % 19 == 0 and cont % 20 == 0:
        print(cont)
        break