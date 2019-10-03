"""21- Faça um programa que receba dois números. Calcule e mostre:
a) a soma dos números pares desse intervalo de números, incluindo os números
digitados;
b) a multiplicação dos números ímpares desse intervalo, incluindo os digitados;"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = 0
multiplicacao = 1

if num1 < num2:
    for n in range(num1, num2+1):
        if n % 2 == 0:
            print(f"Número par: {n}.")
            soma = soma + n
    for n in range(num1, num2+1):
        if n % 2 != 0:
            print(f"Número impar: {n}.")
            multiplicacao = multiplicacao * n
elif num1 > num2:
    for n in range(num2, num1+1):
        if n % 2 == 0:
            print(f"Número par: {n}.")
            soma = soma + n
    for n in range(num2, num1+1):
        if n % 2 != 0:
            print(f"Número impar: {n}.")
            multiplicacao = multiplicacao * n
else:
    print("Não há intervalo entre os números.")

print(f"A soma entre os números pares da diferença entre os números digitados é {soma}.")
print(f"A multiplicação entre os números impares da diferença entre os números digitados é {multiplicacao}.")