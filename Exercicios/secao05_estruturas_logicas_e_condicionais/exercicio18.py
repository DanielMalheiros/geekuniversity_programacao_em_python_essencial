"""18- Faça um programa que mostre ao usuário um menu com 4 opções de operações
matemáticas. O usuário escolhe uma das opções e o programa então pede dois
valores numéricos e realiza a operação, mostrando o resultado."""

operacao = input("Escolha uma operação matemática:\n1- Soma;\n2- Subtração;\n"
                 "3- Multiplicação;\n4- Divisão;\n")

if operacao == '1':
    print("Operação 1- Soma selecionada")
    num1 = float(input("Selecione o primeiro valor: "))
    num2 = float(input("Selecione o segundo valor: "))
    print(f"Resultado: {num1 + num2}")
elif operacao == '2':
    print("Operação 2- Subtração selecionada")
    num1 = float(input("Selecione o primeiro valor: "))
    num2 = float(input("Selecione o segundo valor: "))
    print(f"Resultado: {num1 - num2}")
elif operacao == '3':
    print("Operação 3- Multiplicação selecionada")
    num1 = float(input("Selecione o primeiro valor: "))
    num2 = float(input("Selecione o segundo valor: "))
    print(f"Resultado: {num1 * num2}")
elif operacao == '4':
    print("Operação 4- Divisão selecionada")
    num1 = float(input("Selecione o dividendo: "))
    num2 = float(input("Selecione o denominador: "))
    if num2 != 0:
        print(f"Resultado: {num1 / num2}")
    else:
        print("Denominador deve ser diferente de zero.")
else:
    print("Entrada inválida.")
