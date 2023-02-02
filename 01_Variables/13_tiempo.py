'''Solicitar tiempo en segundos y transformar a horas y minutos. '''
segundos=float(input('Ingrese cantidad en segundos: '))
DIVISOR=60
minutos=segundos/DIVISOR
horas=minutos/DIVISOR
print('Horas: ',horas)
print('Minutos: ',minutos)