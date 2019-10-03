"""41- Faça uma tabela que calcule o IMC de uma pessoa e mostre sua classificação de acordo
com a tabela abaixo:
IMC             CLASSIFICAÇÃO
<18,5            Abaixo do peso
18,6 - 24,9      Saudável
25,0 - 29,9      Peso em excesso
30,0 - 34,9      Obesidade Grau I
35,0 - 39,9      Obesidade Grau II(severa)
>= 40,0          Obesidade Grau III(mórbida)
"""

altura = float(input("Qual sua altura? (1.70, 1.80, etc)"))
peso = float(input("Qual seu peso em quilos? "))
imc = peso / (altura ** 2)

if imc < 18.6:
    print("Abaixo do peso.")
elif 18.6 <= imc < 25:
    print("Saudável")
elif 25 <= imc < 30:
    print("Peso em excesso")
elif 30 <= imc < 35:
    print("Obesidade Grau I")
elif 35 <= imc < 40:
    print("Obesidade Grau II (Severa)")
elif imc <= 40:
    print("Obesidade Grau III (Mórbida")
