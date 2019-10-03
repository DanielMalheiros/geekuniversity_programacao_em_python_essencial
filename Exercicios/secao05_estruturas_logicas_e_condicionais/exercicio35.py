"""35- Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre
1 e 12, se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos e
28 em anos não bissextos."""

dia = int(input("Qual dia? "))
mes = int(input("Qual mês? "))
ano = int(input("Que ano? "))

if dia <= 0 or dia > 31 or mes <= 0 or mes > 12:
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
