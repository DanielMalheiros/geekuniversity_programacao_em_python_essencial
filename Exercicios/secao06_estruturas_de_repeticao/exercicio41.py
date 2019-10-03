"""41- Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos pelo
usuário via teclado. O programa continuará pedindo valores e calculando até que o usuário entre
com um valor 0.
R = R1 * R2 / R1 + R2"""

r1 = int(input("Digite um valor R1: "))
r2 = int(input("Digite um valor R2: "))

while True:
    r = (r1 * r2) / r1 + r2
    print(f"A associação em paralelo destes dois resistores será de {r}.")
    r1 = int(input("Digite um valor R1: "))
    if r1 == 0:
        break
    r2 = int(input("Digite um valor R2: "))
    if r2 == 0:
        break
