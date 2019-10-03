"""10- Faça um programa que calcule e mostre a soma dos 50 primeiros números pares."""

num = 0

for n in range(0, 101):
    if n % 2 == 0:
        num = num + n

print(num)