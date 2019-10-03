"""32- Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como
saída o número de cada dado e a relação entre eles (>,<.=) de cada lançamento."""

# FORMA 1 - Armazenando os valores e comparando depois

num1 = []
num2 = []
v = int(input('Quantas comparações serão feitas? '))
for n in range(v):
    num1.append(input('Digite o primeiro valor: '))
    num2.append(input('Digite o segundo valor: '))
print('### COMPARANDO RESULTADOS ###')
for n in range(v):
    if num1[n] == num2[n]:
        print(f'{num1[n]} = {num2[n]}')
    elif num1[n] < num2[n]:
        print(f'{num1[n]} < {num2[n]}')
    else:
        print(f'{num1[n]} > {num2[n]}')

# FORMA 2 - Comparando os valores conforme vão sendo digitados

v = int(input('Quantas comparações serão feitas? '))
for n in range(v):
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    if num1 == num2:
        print(f'{num1} = {num2}')
    elif num1 < num2:
        print(f'{num1} < {num2}')
    else:
        print(f'{num1} > {num2}')
