"""37- Escreva um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a seguinte
propriedade: a soma dos dois dígitos de mais baixa ordem com os dois dígitos de mais alta ordem elevada ao
quadrado é igual ao proprio número. Por exemplo: para o inteiro 3025, temos que: 30 + 25 = 55 e 55 ** 2 = 3025."""

for i in range(1000, 10000):
    n1 = int(str(i)[0:2])
    n2 = int(str(i)[2:4])
    if (n1 + n2)**2 == i:
        print(i)