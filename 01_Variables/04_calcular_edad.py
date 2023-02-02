'''Programa que permita calcular la edad de una persona conociendo el año 
actual y el usuario digita su año de nacimiento.'''

AÑO_ACTUAL=2023
print('Año actual: ',AÑO_ACTUAL)
año_nacimiento=int(input('Digite su año de nacimiento para calcular la edad: '))
edad= AÑO_ACTUAL-año_nacimiento
print(edad)
