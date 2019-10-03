#  48- Leia um valor inteiro em segundos e imprima-o em horas, minutos e segundos.

seg = int(input("Insira uma quantidade de segundos: "))
print(f"{seg} segundos equivalem a {seg / 60:.2f} minutos e a {seg / 3600:.2f} horas.")
