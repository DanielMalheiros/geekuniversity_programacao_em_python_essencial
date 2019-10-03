"""38- Faça um programa que calcule o terno pitagórico a,b,c, para qual a + b + c = 1000. Um terno pitagórico
é um conjunto de três números naturais para qual a ** 2 + c ** 2 = c ** 2, por exemplo:
3 ** 2 + 4 ** 2 = 5 ** 2"""

for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = 1000 - a - b
        if ((a*a) + (b*b)) == (c*c):
            print(a, b, c)