"""44- Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo."""

degrau = int(input("Insira a altura do degrau em centímetros: "))
altura = float(input("Insira a altura que deseja subir em centímetros: "))
if altura > 0 and degrau > 0:
    print(f"Você subirá {altura / degrau} degraus.")
