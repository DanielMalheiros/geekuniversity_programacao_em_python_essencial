"""30- Faça um programa para calcular as seguintes sequências:
1 + 2 + 3 + 4 + 5+....+n
1 - 2 + 3 - 4 + 5+...+ (2n-1)
1 + 3 + 5 + 7+...(2n - 1)"""

n = int(input("Insira um número inteiro e positivo: "))
s1 = 0
s2 = 0
s3 = 0

if n > 0:
    #  sequencia 1:
    for i in range(n+1):
        s1 += i
    for i in range(2 * n):
        if i % 2 == 0:
            s2 -= i
        else:
            s2 += i
    for i in range(2 * n):
        if i % 2 != 0:
            s3 += i
else:
    print("Número inválido.")

print(f"O resultado da primeira sequencia é {s1}")
print(f"O resultado da segunda sequencia é {s2}")
print(f"O resultado da terceira sequencia é {s3}")