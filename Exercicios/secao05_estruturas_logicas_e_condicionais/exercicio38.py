"""38- Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros:
Dia, Mês, Ano. Teste a validade desta data para saber se esta é uma data válida. Teste se
o dia fornecido é um dia valido atentando para anos bissextos, se o mês fornecido é um mês
valido e se o ano fornecido é um ano valido (ano > ano atual) considerando ano uma constante
com valor 2008. Imprimir: "data válida" ou "data inválida" no final da execução do programa.
"""

dia = int(input("Qual dia? "))
mes = int(input("Qual mês? "))
ano = int(input("Que ano? "))

if dia <= 0 or dia > 31 or mes <= 0 or mes > 12 or ano > 2008:
    print("Data inválida.")
elif mes == 4 or mes == 6 or mes == 7 or mes == 9 or mes == 11:
    if dia >= 31:
        print("Data inválida.")
elif mes == 2:
    if ano % 4 == 0 and ano % 100 != 0:
        if dia > 29:
            print("Data inválida.")
    else:
        if dia > 28:
            print("Data inválida.")
else:
    print("Data valida.")
