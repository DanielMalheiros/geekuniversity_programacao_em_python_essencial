"""w6- Leia uma distância em KM e a quantidade de litros de gasolina consumidos por
 um carro em eum percurso, calcule o consumo de Km/L e escreva uma mensagem de acordo
 com a tabela abaixo.
 CONSUMO                 Km/l               MENSAGEM
 menor que                8               Venda o carro!
 entre                  8 e 11             Econômico!
 maior que               12              Super econômico!
 """

km = float(input("Insira uma distancia em quilômetros: "))
li = float(input("Quants litros de gasolina são consumida nessa distancia? "))

if km / li < 8:
    print("Venda o carro!")
elif km / li >= 8 and km / li < 12:
    print("Econômico!")
else:
    print("Super econômico!")
