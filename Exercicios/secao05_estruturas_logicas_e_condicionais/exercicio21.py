"""21- Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação
 escolhida. Escreva uma mensagem de erro de a opção for inválida.

 Escolha a opção:
 1- Soma de 2 números.
 2- Diferença entre 2 números (maior pelo menor)
 3- Produto entre 2 números.
 4- Divisão entre 2 números (o denominador não pode ser zero)."""

opcao = input("Escolha a opção:\n1-Soma de 2 números.\n2- Diferença entre 2 números (maior pelo menor))\n"
              "3- Produto entre 2 números.\n4-Divisão entre 2 números (o denominador não pode ser zero)")
if opcao == '1':
    print("Opção 1: Soma de 2 números escolhida.")
    num1 = float(input("Defina o primeiro valor: "))
    num2 = float(input("Defina o segundo valor: "))
    print(f"A soma entre {num1} e {num2} é {num1 + num2}")
elif opcao == '2':
    print("Opção 2: Diferença entre 2 números (maior pelo menor) escolhida. ")
    num1 = float(input("Defina o primeiro valor: "))
    num2 = float(input("Defina o segundo valor: "))
    if num1 > num2:
        print(f"A diferença entre {num1} e {num2} é {num1 - num2}")
    elif num2 > num1:
        print(f"A diferença entre {num2} e {num1} é {num2 - num1}")
    else:
        print("Os valores são iguais.")
elif opcao == '3':
    print("Opção 3: Produto entre dois números escolhida. ")
    num1 = float(input("Defina o primeiro valor: "))
    num2 = float(input("Defina o segundo valor: "))
    print(f"O produto entre {num1} e {num2} é {num1 * num2}")
elif opcao == '4':
    print("Opção 4: Divisão entre 2 números (o denominador não pode ser zero). ")
    num1 = float(input("Defina o valor a ser dividendo: "))
    num2 = float(input("Defina o denominador: "))
    if num2 != 0:
        print(f"A divisão de {num1} por {num2} é {num1 / num2}")
else:
    print("Opção inválida.")
