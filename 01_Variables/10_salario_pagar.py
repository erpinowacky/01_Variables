'''Programa que permita determinar el salario a pagar a un empleado, teniendo como entradas
 el salario diario y el número de días trabajados. Tenga en cuenta que al empleado se le debe descontar 
 el 10% por concepto de pensión y 15% por concepto de salud.'''

DES_PENSION=10/100
DES_SALUD=15/100
salarioDiario=float(input('Digite el salario diario: '))
diasTrabajados=int(input('Ingrese número de dias trabajados: '))
salario_a_pagar=salarioDiario*diasTrabajados
salario_a_pagar=salario_a_pagar-((salario_a_pagar*DES_PENSION)+(salario_a_pagar*DES_SALUD))
print('El trabajador recibe el saldo total de: $',salario_a_pagar)
