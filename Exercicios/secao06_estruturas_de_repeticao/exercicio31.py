"""31- Faça um programa que calcule e escreva o valor de S:
S = 1/1 + 3/2 + 5/3 + 7/4...99/50"""

s1 = 0    # divisor
s2 = 0    # denominador

for n in range(100):
    s1 += n
for n in range(50+1):
    s2 += n

s = s1 / s2
print(s)
