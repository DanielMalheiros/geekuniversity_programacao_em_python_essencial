"""49- O funcionario chamado Carlos tem um colega chamado João que recebe um salário que equivale a
1/3 do seu salário. Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário
integralmente nela, pois está rendendo 2% ao mês. João aplicará seu salário integralmente no fundo de
renda fixa, que está rendendo 5% ao mês. Construa um programa que deverá calcular e mostrar a quantidade
de meses necessarios para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos."""

salario_a = float(input("Defina o salario de Carlos: "))
salario_b = salario_a / 3
contador = 1
poupanca_a = 0
poupanca_b = 0
poupanca_a = (poupanca_a + salario_a) * 1.02
poupanca_b = (poupanca_b + salario_b) * 1.05

while poupanca_b < poupanca_a:
    poupanca_a = (poupanca_a + salario_a) * 1.02
    poupanca_b = (poupanca_b + salario_b) * 1.05
    contador += 1

print(contador)
