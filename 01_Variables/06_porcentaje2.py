'''Programa que permita calcular el 30%, el 60% y el 90% de cualquier número.'''

porcentaje1=30/100
porcentaje2=60/100
porcentaje3=90/100

num=float(input('Digite un número para calcular el 30%, 60% y el 90% respectivamente: '))
calculo1=num*porcentaje1
calculo2=num*porcentaje2
calculo3=num*porcentaje3
str(num)
str(calculo1)
str(calculo2)
str(calculo3)

print(f'Número: {num}')
print(f'El 30% es: {calculo1}')
print(f'El 60% es: {calculo2}')
print(f'El 90% es: {calculo3}')

