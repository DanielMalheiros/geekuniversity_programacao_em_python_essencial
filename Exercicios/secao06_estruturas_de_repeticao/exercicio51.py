"""51- Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000. Em 1996 recebeu um aumento
de 1.5%. A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior. Faça um
programa que determine o salário atual do funcionario."""

aumento = 1.015
salario = 2000
for ano in range(1996, 2019+1):
    salario = salario * aumento
    aumento = aumento * 2

print(salario)
