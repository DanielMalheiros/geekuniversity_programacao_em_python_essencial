"""49- Faça um programa para ler o horário (hora, minuto e segundo) de inicio e a duração, em segundos
de uma experiência biológica. O programa deve resultar com o novo horário (hora, minuto e segundo)
do termino da mesma."""

horainicio = int(input('Digite a hora de início: '))
minutosinicio = int(input('Digite os minutos de início: '))
segundosinicio = int(input('Digite os segundos de início: '))
print(f'O horário de início do experimento é {horainicio}:{minutosinicio}:{segundosinicio}h')
duracao = int(input('Digite a duração do experimento em segundos: '))

segundos = (horainicio * 3600) + (minutosinicio * 60) + segundosinicio + duracao

hora2 = segundos // 3600
minuto2 = (segundos % 3600) // 60
segundo2 = (segundos % 3600) % 60

print(f'A experiência terminará as {hora2}:{minuto2}:{segundo2}h')
