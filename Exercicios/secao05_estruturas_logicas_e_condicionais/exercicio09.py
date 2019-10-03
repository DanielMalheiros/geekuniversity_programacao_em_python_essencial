"""9- Leia o salário de um trabalhador e o valor da prestação de um emprestimo. Se a
prestação for maior que 20% do salário imprima "Empréstimo não concedido", caso
contrário, imprima "Empréstimo concedido."""

salario = float(input("Insira o valor de seu salário em reais: "))
p = float(input("Insira o valor da prestação em reais: "))

if salario / 5 < p:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")