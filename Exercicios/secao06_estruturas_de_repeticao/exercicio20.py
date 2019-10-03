"""20- Ler uma sequência de números inteiros e determinar se são pares ou não. Deverá ser
informado o número de dados lidos e número de valores pares. O processo termina quando for
digitado o número 1000."""

num = int(input("Insira um número: "))
lidos = 0
pares = 0

while num != 1000:
    lidos = lidos + 1
    if num % 2 == 0:
        pares = pares + 1
    num = int(input("Insira um número: "))

print(f"dos {lidos} números lidos, {pares} são pares.")