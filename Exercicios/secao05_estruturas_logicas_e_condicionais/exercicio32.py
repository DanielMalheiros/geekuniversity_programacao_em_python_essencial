"""32- Escrever um programa que leia o código do produto escolhido do cardápio de uma
lanchonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um pedido. O cardapio da lanchonete
segue o padrão abaixo:
Especificação           Código        Preço
Cachorro Quente          100          1.20
Bauru Simples            101          1.30
Bauru com Ovo            102          1.50
Hamburguer               103          1.20
Cheeseburguer            104          1.70
Suco                     105          2.20
Refrigerante             106          1.00
"""

soma = 0
codigo = input("O que deseja pedir do cardapío abaixo?\n"
               "Especificação           Código        Preço\n"
               "Cachorro Quente          100          1.20\n"
               "Bauru Simples            101          1.30\n"
               "Bauru com Ovo            102          1.50\n"
               "Hamburguer               103          1.20\n"
               "Cheeseburguer            104          1.70\n"
               "Suco                     105          2.20\n"
               "Refrigerante             106          1.00\n"
               "Para selecionar o lanche, entre seu respectivo código.\n"
               "Para finalizar pedido, use o código 0 (zero).")

while codigo != '0':
    if codigo == '100':
        q = int(input("Cachorro quente selecionado.\nQuantos?"))
        soma = soma + q * 1.20
        fim = input("Deseja pedir algo mais? (S/N)")
        if fim.lower() == 's':
            codigo = input("O que mais deseja pedir do cardapío?")
        elif fim.lower() == 'n':
            print("Pedido finalizado.")
            codigo = '0'
        else:
            print("Comando inválido. Reinicie o programa.")
    elif codigo == '101':
        q = int(input("Bauru simples selecionado.\nQuantos?"))
        soma = soma + q * 1.30
        fim = input("Deseja pedir algo mais? (S/N)")
        if fim.lower() == 's':
            codigo = input("O que mais deseja pedir do cardapío?")
        elif fim.lower() == 'n':
            print("Pedido finalizado.")
            codigo = '0'
        else:
            print("Comando inválido. Reinicie o programa.")
    elif codigo == '102':
        q = int(input("Bauru com ovo selecionado.\nQuantos?"))
        soma = soma + q * 1.50
        fim = input("Deseja pedir algo mais? (S/N)")
        if fim.lower() == 's':
            codigo = input("O que mais deseja pedir do cardapío?")
        elif fim.lower() == 'n':
            print("Pedido finalizado.")
            codigo = '0'
        else:
            print("Comando inválido. Reinicie o programa.")
    elif codigo == '103':
        q = int(input("Hamburguer selecionado.\nQuantos?"))
        soma = soma + q * 1.20
        fim = input("Deseja pedir algo mais? (S/N)")
        if fim.lower() == 's':
            codigo = input("O que mais deseja pedir do cardapío?")
        elif fim.lower() == 'n':
            print("Pedido finalizado.")
            codigo = '0'
        else:
            print("Comando inválido. Reinicie o programa.")
    elif codigo == '104':
        q = int(input("Bauru com ovo selecionado.\nQuantos?"))
        soma = soma + q * 1.70
        fim = input("Deseja pedir algo mais? (S/N)")
        if fim.lower() == 's':
            codigo = input("O que mais deseja pedir do cardapío?")
        elif fim.lower() == 'n':
            print("Pedido finalizado.")
            codigo = '0'
        else:
            print("Comando inválido. Reinicie o programa.")
    elif codigo == '105':
        q = int(input("Suco selecionado.\nQuantos?"))
        soma = soma + q * 2.20
        fim = input("Deseja pedir algo mais? (S/N)")
        if fim.lower() == 's':
            codigo = input("O que mais deseja pedir do cardapío?")
        elif fim.lower() == 'n':
            print("Pedido finalizado.")
            codigo = '0'
        else:
            print("Comando inválido. Reinicie o programa.")
    elif codigo == '106':
        q = int(input("Refrigerante selecionado.\nQuantos?"))
        soma = soma + q * 1.00
        fim = input("Deseja pedir algo mais? (S/N)")
        if fim.lower() == 's':
            codigo = input("O que deseja pedir do cardapío abaixo?")
        elif fim.lower() == 'n':
            print("Pedido finalizado.")
            codigo = '0'
        else:
            print("Comando inválido. Reinicie o programa.")

end = input("Finalizar pedido? (S/N)")
if end.lower() == 's':
    print(f"Pedido finalizado. O valor total será de R${soma:.2f}.")
elif end.lower() == 'n':
    codigo = input("O que mais deseja pedir do cardapío?")
else:
    print("Comando inválido. Reiniciar programa.")
