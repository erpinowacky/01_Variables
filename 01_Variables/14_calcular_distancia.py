'''Solicitar al usuario una distancia en metros y transformar a km., cm. y mm. '''

KILOMETRO=1000
CENTIMETRO=100
MILIMETRO=1000
distancia=float(input('Digite la distancia en metros: '))
distanciaKm=distancia/KILOMETRO
distancia_cm=distancia*CENTIMETRO
distancia_mm=distancia*MILIMETRO
print('La distancia en Km: ',distanciaKm)
print('La distancia en cm: ',distancia_cm)
print('La distancia en mm: ',distancia_mm)
