'''Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios
 elementos de la misma referencia. Debe tener como entradas el valor unitario, la cantidad de productos 
 comprados y al valor final se debe adicionar el 16% correspondiente al IVA.'''

IVA=16/100
referencia=''
valorUnitario=0
cantidadProductos=0
valorFinal=0
referencia=input('Digite referencia del producto: ')
valorUnitario=float(input('Ingrese valor del producto: '))
cantidadProductos=int(input('Cantidad de productos: '))
valorFinal=valorUnitario*cantidadProductos
valorFinal=valorFinal+(valorFinal*IVA)
print('El valor total a pagar del producto con referencia',referencia,' es de $',valorFinal)




