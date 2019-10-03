"""24- Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
possui uma taxa diferente de imposto sobre o produto (MG 7%, SP 12%, RJ 15%, MS 8%).
Faça um programa em que o usuário entre com o valor e o estado destino do produto e
o programa retorne o preço final do produto acrescido do imposto do estado em que ele
será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro."""

valor_base = float(input("Defina o valor base (sem imposto) do produto que será vendido: "))
destino = input("Para qual cidade o produto será vendido?\n1- MG\n2- SP\n3- RJ\n4- MS")

if destino == '1':
    valor_mg = valor_base * 1.07
    print(f"O valor acrescido do imposto de MG será R${valor_mg}.")
elif destino == '2':
    valor_sp = valor_base * 1.12
    print(f"O valor acrescido do imposto de SP será R${valor_sp}.")
elif destino == '3':
    valor_rj = valor_base * 1.15
    print(f"O valor acrescido de imposto do RJ será R${valor_rj}.")
elif destino == '4':
    valor_ms = valor_base * 1.08
    print(f"O valor acrescido do imposto de MS será R${valor_ms}.")
else:
    print("Destino inválido.")
