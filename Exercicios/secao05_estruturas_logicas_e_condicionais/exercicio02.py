"""2- Leia um número fornecido pelo usuário. Se esse número for positivo,
calcule a raiz quadrada do número. Se for negativo, mostre uma mensagem
dizendo que o número é invalido."""

num = int(input("Escolha um número: "))

if num < 0:
    print("Número invalido.")
else:
    print(f"A raiz quadrada de {num} é {num ** (1/2):.2f}.")
