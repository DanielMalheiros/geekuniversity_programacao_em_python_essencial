"""39- Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que
considera o salário atual e o tempo de serviço de cada funcionario. Os funcionários com
menor salário terão um aumento proporticonalmente maior do que os funcionários com um maior
salário, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus adicional
de salário. Faça um programa que leia:
-o valor do salário atual do funcionario;
-o tempo de serviço desse funcionário na empresa em anos de trabalho;
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor
do salário final reajustadoo, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.
SALARIO ATUAL            REAJUSTE(%)          TEMPO DE SERVIÇO           BÔNUS
Até 500,00                 25%                 abaixo de 1 ano         Sem bonus
Até 1000,00                20%                 de 1 a 3 anos            100,00
Até 1500,00                15%                 de 4 a 6 anos           200,00
Até 2000,00                10%                 De 7 a 10 anos           300,00
Acima de 2000,00        Sem reajuste           Mais de 10 anos          500,00
"""

tempo = int(input("A quantos anos você trabalha na empresa? "))
salario = float(input("Qual o valor de seu salário em reais? "))

if salario < 500:
    if tempo < 1:
        print(f"Seu novo salário será de R${salario * 1.25}")
    elif 1 <= tempo <= 3:
        print(f"Seu novo salário será de R${salario * 1.25 + 100}")
    elif 4 <= tempo <= 6:
        print(f"Seu novo salário será de R${salario * 1.25 + 200}")
    elif 7 <= tempo <= 10:
        print(f"Seu novo salário será de R${salario * 1.25 + 300}")
    elif tempo > 10:
        print(f"Seu novo salário será de R${salario * 1.25 + 500}")
elif 500 <= salario < 1000:
    if tempo < 1:
        print(f"Seu novo salário será de R${salario * 1.20}")
    elif 1 <= tempo <= 3:
        print(f"Seu novo salário será de R${salario * 1.20 + 100}")
    elif 4 <= tempo <= 6:
        print(f"Seu novo salário será de R${salario * 1.20 + 200}")
    elif 7 <= tempo <= 10:
        print(f"Seu novo salário será de R${salario * 1.20 + 300}")
    elif tempo > 10:
        print(f"Seu novo salário será de R${salario * 1.20 + 500}")
elif 1000 <= salario < 1500:
    if tempo < 1:
        print(f"Seu novo salário será de R${salario * 1.15}")
    elif 1 <= tempo <= 3:
        print(f"Seu novo salário será de R${salario * 1.15 + 100}")
    elif 4 <= tempo <= 6:
        print(f"Seu novo salário será de R${salario * 1.15 + 200}")
    elif 7 <= tempo <= 10:
        print(f"Seu novo salário será de R${salario * 1.15 + 300}")
    elif tempo > 10:
        print(f"Seu novo salário será de R${salario * 1.15 + 500}")
elif 1500 <= salario <= 2000:
    if tempo < 1:
        print(f"Seu novo salário será de R${salario * 1.10}")
    elif 1 <= tempo <= 3:
        print(f"Seu novo salário será de R${salario * 1.1 + 100}")
    elif 4 <= tempo <= 6:
        print(f"Seu novo salário será de R${salario * 1.10 + 200}")
    elif 7 <= tempo <= 10:
        print(f"Seu novo salário será de R${salario * 1.10 + 300}")
    elif tempo > 10:
        print(f"Seu novo salário será de R${salario * 1.10 + 500}")
elif salario > 2000:
    if tempo < 1:
        print(f"Seu novo salário será de R${salario}")
    elif 1 <= tempo <= 3:
        print(f"Seu novo salário será de R${salario + 100}")
    elif 4 <= tempo <= 6:
        print(f"Seu novo salário será de R${salario + 200}")
    elif 7 <= tempo <= 10:
        print(f"Seu novo salário será de R${salario + 300}")
    elif tempo > 10:
        print(f"Seu novo salário será de R${salario + 500}")
