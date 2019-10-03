"""40- Uma empresa contrata um encadador a R$30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que devera ser
paga, sabendo-se que são descontados 8% para o imposto de renda."""

num = int(input("Quantos dias o encanador trabalhou? "))
salario_liq = (num * 30) * 0.92
print(f"Salário líquido do encanador: {salario_liq} reais. ")
