"""26- Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número
dado."""

num = int(input("Insira um número: "))

for n in range(num, 999999999):
    if n % 11 == 0 or n % 13 == 0 or n % 17 == 0:
        print(n)
        break