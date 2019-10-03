"""44- Leia um número positivo do usuário, então calcule e imprima a sequência Fibonacci até
o primeiro número superior ao número lido. Exemplo: se o usuário informou o número 30, a sequencia
a ser impressa sera 0 1 1 2 3 5 8 13 21 34."""

num = int(input("Digite um número inteiro e positivo: "))
if num > 0:
    t1 = 0
    t2 = 1
    print(f"{t1} - {t2}",end='')
    while t2 < num:
        t3 = t1 + t2
        print(f" - {t3}",end='')
        t1 = t2
        t2 = t3
else:
    print("Número inválido.")
