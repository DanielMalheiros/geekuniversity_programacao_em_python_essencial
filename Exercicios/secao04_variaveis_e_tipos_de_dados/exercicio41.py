"""41- Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas
no mês. Imprima o valor a ser pago ao funcionario adicionando 10% sobre o valor calculado."""

horas = int(input("Quantas horas você trabalhou neste mês? "))
valor = float(input("Qual o valor pago por hora, em reais? "))
print(f"Seu salário acrescido de 10% será {(horas * valor) * 1.1}")
