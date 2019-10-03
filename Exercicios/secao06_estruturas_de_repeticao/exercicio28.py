"""28- Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E,
de acordo com a fórmula a seguir:
E = 1 + 1/1! + 1/2! + 1/3! + 1/N!"""

n = int(input("Insira um valor N inteiro e positivo: "))
e = 1

if n > 0:
    for x in range(1, n+1):
        f = 1     # multiplicador para fatorial
        cont = x
        for x in range(n, 0, -1):
            while cont > 0:
                f = f * cont
                cont -= 1
        e += 1/f
else:
    print("Número invalido.")

print(e)
