"""52- Escreva um programa que receba como entrada o valor do saque realizado pelo cliente
de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque
com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real."""

valor = float(input("Digite o valor desejado: "))
n100 = valor / 100
n50 = (valor % 100) / 50
n10 = (valor % 50) / 10
n5 = (valor % 10) / 5
n2 = (valor % 5) / 2
n1 = (valor % 2) / 1

print(f"Total de notas de 100: {int(n100)}\nTotal de notas de 50: {int(n50)}\nTotal de notas de 10: {int(n10)}\n"
      f"Total de notas de 5: {int(n5)}\nTotal de notas de 2: {int(n2)}\nTotal de notas de 1: {int(n1)}")