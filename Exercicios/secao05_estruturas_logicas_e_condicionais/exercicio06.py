"""6- Escreva um programa que, dados dois números inteiros, mostre na tela
qual é o maior deles, assim como a diferença existente entre ambos."""

num1 = int(input("Escolha um valor: "))
num2 = int(input("Escolha mais um valor: "))
if num1 > num2:
    print(f"Maior valor: {num1}     Diferença entre os valores: {num1 - num2}")
elif num1 < num2:
    print(f"Maior valor: {num2}     Diferença entre os valores: {num2 - num1}")
else:
    print("Os valores são iguais.")