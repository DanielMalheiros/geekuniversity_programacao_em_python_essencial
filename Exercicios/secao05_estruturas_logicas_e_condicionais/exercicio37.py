"""37- As tarifas de um certo parque de estacionamento são as seguintes:
-primeira e segunda hora - R$1,00 cada
-terceira e quarta hora -  R$1,40 cada
-quinta hora e seguintes - R$2,00 cada
O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem
estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria se tivesse
estacionado por 120 minutos. Os momentos de chegada ao parque e partida deste são apresentados
na forma de pares de inteiros, representando horas e minutos. Por exemplo, o par 12 50 representará
"dez para a uma da tarde". Pretende-se criar um programa que, lido pelo teclado os momentos de
chegada e de partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada
e a partida se dão com intervalo não superior a 24 horas. Portanto, se uma data hora de chegada for
superior à da partida, isso não é uma situação de erro, antes significará que a partida ocorreu no
dia seguinte ao da chegada."""

hora_e = int(input("Qual foi a hora de entrada? "))
minuto_e = int(input("Qual foi o minuto? "))
hora_s = int(input("Qual foi a hora de partida? "))
minuto_s = int(input("Qual foi o minuto? "))

if hora_e >= 25 or hora_s >= 25 or minuto_e > 60 or minuto_s > 60 or hora_e < 0 or hora_s < 0 or minuto_e < 0 or\
        minuto_s < 0:
    print("Hora e/ou minuto inválido(s)")

if hora_e < hora_s:
    if minuto_s > 0:
        tempo = hora_s - hora_e + 1
    else:
        tempo = hora_s - hora_e
elif hora_e == hora_s:
    if minuto_e > minuto_s:
        tempo = 24
    if minuto_s > minuto_e or minuto_s == minuto_e:
        print("24 horas ou mais.")
elif hora_s < hora_e:
    if minuto_s > 0:
        tempo = (hora_s + 24) - hora_e + 1
    else:
        tempo = (hora_s + 24) - hora_e

if tempo <= 2:
    print(f"O preço do estacionamento será R${tempo}.")
elif 2 < tempo <= 4:
    preco = (tempo - 2) * 1.40 + 2
    print(f"O preço do estacionamento será R${preco}.")
elif tempo > 4:
    preco = (tempo - 4) * 2 + 2 + 2.80
    print(f"O preço do estacionamento será R${preco}.")
