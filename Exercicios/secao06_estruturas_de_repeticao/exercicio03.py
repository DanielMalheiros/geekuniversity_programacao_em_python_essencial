"""3- Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva
na tela, iniciando em 10 e terminando em 0. Mostrar uma mensagem "Fim!" após o final
da contagem."""

num = 10
while num >= 0:
    print(f"{num}...")
    num = num - 1

print("Fim!")