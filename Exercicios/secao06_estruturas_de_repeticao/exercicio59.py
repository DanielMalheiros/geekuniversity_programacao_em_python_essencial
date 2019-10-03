"""59- Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor
do kwh, e para cada habitante entre com os seguintes dados: consumo do mês e código do consumidor
(1-Residencial,2-Comercial,3-Industrial). No final imprima o maior, menor e a média do consumo
dos habitantes e por fim o total do consumo de cada categoria de consumidor."""

n_hab = int(input("Digite o número de habitantes da cidade X: "))
valor_kwh = float(input("Digite o valor do kwh em reais: "))
maior = 0
menor = 10000000000000
cont_1 = 0
cont_2 = 0
cont_3 = 0
media = 0

for h in range(1, n_hab+1):
    valor = float(input(f"Qual o valor consumido pelo habitante numero {h}?"))
    while valor < 0:
        valor = float(input(f"Valor inválido.\nQual o valor consumido pelo habitante numero {h}?"))
    media += valor
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    codigo = input(f"Insira o código de consumidor do habitante numero {h}:"
                   f"\n1-Residencial\n2-Comercial\n3-Industrial ")
    while codigo != '1' and codigo != '2' and codigo != '3':
        codigo = input(f"Codigo inválido.\n"
                       f"Insira o código de consumidor do habitante numero {h}:"
                       f"\n1-Residencial\n2-Comercial\n3-Industrial ")
    if codigo == '1':
        cont_1 += 1
    elif codigo == '2':
        cont_2 += 1
    elif codigo == '3':
        cont_3 += 1

print(f"O maior valor consumido foi R${maior}, o menor foi R${menor}, a media de consumo entre todos "
      f"os habitantes é de R${media / (cont_1 + cont_2 + cont_3)}. Residenciais: {cont_1}\nComerciais {cont_2}\n"
      f"Industriais: {cont_3}")
