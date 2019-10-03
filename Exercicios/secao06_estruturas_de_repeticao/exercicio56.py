"""56- Faça um programa que calcule a soma de todos os números primos abaixo de dois milhões."""

num = 2000
soma, primo, count = 0, 0, 2

while num > count:
    for n in range(1, count+1):
        if count % n == 0:
            primo += 1
    if primo <= 2:
        #print(count)
        soma += count
    count += 1                  # Contador progressivo
    primo = 0                   # Zera contador depois que o número foi checado
print('Soma = ', soma)