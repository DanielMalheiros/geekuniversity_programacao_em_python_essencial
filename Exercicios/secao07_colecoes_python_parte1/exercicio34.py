"""34- Faça um programa para ler 10 números DIFERENTES a serem armazenados em um vetor. Os dados
deverão ser armazenados no vetor na ordem que forem sendo lidos, sendo que caso o usuário digite
um número que já foi digitado anteriormente, o programa deverá pedir para ele digitar outro número.
Note que cada valor digitado pelo usuário deve ser pesquisado no vetor, verificando se ele existe entre
os números que já foram fornecidos. Exibir na tela o vetor final que foi digitado."""

contador = 0
vetor = []

while contador < 10:
    valor = int(input(f"Digite um valor para o vetor ({contador+1}/10): "))
    if valor in vetor:
        print("Este número já foi digitado anteriomente! Digite outro número.")
    else:
        vetor.append(valor)
        contador += 1

print(vetor)
