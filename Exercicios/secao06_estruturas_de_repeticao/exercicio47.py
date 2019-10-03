"""47- Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre
dois números. O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição
do resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção de
sadía (opção 5).
1-  Adição
2 -Subtração
3- Multiplicação
4- Divisão
5- Saida"""

num1 = int(input("Bem vindo ao calculador MALHEIROS!\nInsira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

opc = input("Para adição, digite 1.\nPara subtração, digite 2.\n"
            "Para multiplsicação, digite 3.\nPara divisão, digite 4.\nPara sair do programa, digite 0.")
while opc != '5':
    if opc == '1':
        print(f"Adição selecionada.\nA soma entre {num1} e {num2} é {num1 + num2}")
        opc2 = input("Deseja continuar calculando? (S/N)")
        while opc2.lower() != 's' and opc2.lower() != 'n':
            opc2 = input("Opção inválida.\nDeseja continuar calculando? (S/N)")
        if opc2.lower() == 's':
            opc = input("Para adição, digite 1.\nPara subtração, digite 2.\n"
                        "Para multiplicação, digite 3.\nPara divisão, digite 4.\nPara sair do programa, digite 5.")
        elif opc2.lower() == 'n':
            opc = '5'
    elif opc == '2':
        print(f"Subtração selecionada.\nA subtração entre {num1} e {num2} é {num1 - num2}")
        opc2 = input("Deseja continuar calculando? (S/N)")
        while opc2.lower() != 's' and opc2.lower() != 'n':
            opc2 = input("Opção inválida.\nDeseja continuar calculando? (S/N)")
        if opc2.lower() == 's':
            opc = input("Para adição, digite 1.\nPara subtração, digite 2.\n"
                        "Para multiplicação, digite 3.\nPara divisão, digite 4.\nPara sair do programa, digite 5.")
        elif opc2.lower() == 'n':
            opc = '5'
    elif opc == '3':
        print(f"Multiplicação selecionada.\nA multiplicação entre {num1} e {num2} é {num1 * num2}")
        opc2 = input("Deseja continuar calculando? (S/N)")
        while opc2.lower() != 's' and opc2.lower() != 'n':
            opc2 = input("Opção inválida.\nDeseja continuar calculando? (S/N)")
        if opc2.lower() == 's':
            opc = input("Para adição, digite 1.\nPara subtração, digite 2.\n"
                        "Para multiplicação, digite 3.\nPara divisão, digite 4.\nPara sair do programa, digite 5.")
        elif opc2.lower() == 'n':
            opc = '5'
    elif opc == '4':
        print(f"Divisão selecionada.\nA divisão entre {num1} e {num2} é {num1 / num2}")
        opc2 = input("Deseja continuar calculando? (S/N)")
        while opc2.lower() != 's' and opc2.lower() != 'n':
            opc2 = input("Opção inválida.\nDeseja continuar calculando? (S/N)")
        if opc2.lower() == 's':
            opc = input("Para adição, digite 1.\nPara subtração, digite 2.\n"
                        "Para multiplicação, digite 3.\nPara divisão, digite 4.\nPara sair do programa, digite 5.")
        elif opc2.lower() == 'n':
            opc = '5'
    else:
        opc = input("Comando inválido.\nPara adição, digite 1.\nPara subtração, digite 2.\n"
                    "Para multiplicação, digite 3.\nPara divisão, digite 4.\nPara sair do programa, digite 5. ")
