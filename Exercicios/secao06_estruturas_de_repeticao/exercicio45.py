"""45- Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice versa.
Você deve criar um menu com as duas opções de conversão e com uma opção para finalizar o programa.
O usuário poderá fazer quantas conversões desejar, sendo que o programa só será finalizado quando a opção
de finalizar for escolhida."""

opc = input("Bem vindo ao conversor de velocidade.\nPara converter km/h para m/s, digite 1.\n"
            "Para converter m/s para km/h, digite 2.\nPara finalizar o programa, digite 0.")
while opc != '0':
    if opc != '1' and opc != '2':
        print("Opção inválida.")
        opc = input("Para converter km/h para m/s, digite 1.\n"
                    "Para converter m/s para km/h, digite 2.\nPara finalizar o programa, digite 0.")
    if opc == '1':
        kmh = float(input("Insira a velocidade em km/h: "))
        print(f"{kmh}km/h são {kmh / 3.6:.2f}m/s.")
        opc = input("Para converter outro valor km/h para m/s, digite 1.\n"
                    "Para converter outro valor m/s para km/h, digite 2.\nPara finalizar o programa, digite 0.")
    elif opc == '2':
        ms = float(input("Insira a velocidade em m/s: "))
        print(f"{ms}/ms são {ms * 3.6}km/h.")
        opc = input("Para converter outro valor km/h para m/s, digite 1.\n"
                    "Para converter outro valor m/s para km/h, digite 2.\nPara finalizar o programa, digite 0.")