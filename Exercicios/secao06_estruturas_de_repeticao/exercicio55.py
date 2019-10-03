"""55-  Escreva um programa que leia um inteiro não negativo n e imprima a soma
dos n primeiros números primos."""

num = int(input('Digite um número: '))
soma, primo, x, count = 0, 0, 0, 2

while num > x:
    for n in range(1, count+1):
        if count % n == 0:
            primo += 1
    if primo <= 2:
        print(count)
        soma += count
        x += 1                  # Define a quantidade de números primos devem ser gerados
    count += 1                  # Contador progressivo
    primo = 0                   # Zera contador depois que o número foi checado
print('Soma = ', soma)