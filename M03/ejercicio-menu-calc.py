import os
os.system('clear')

print 'Que desea hacer el amo?'
print '1- Sumar'
print '2- Restar'
print '3- Multiplicar'
print '4- Dividir'
print '5- Salir'

opcion = input("Elija una opcion: ")

if opcion == 5:
	print 'Hasta otra!'


if opcion == 1:
	
	numero1 = input("Introduce un numero para sumar: ")
	numero2 = input("Introduce otro numero: ")
	sumar = numero1 + numero2
	
	print 'El resultado es: ', sumar

if opcion == 2:
	
	numero1 = input("Introduce un numero para restar: ")
	numero2 = input("Introduce otro numero: ")
	restar = numero1 - numero2
	
	print 'El resultado es: ', restar

if opcion == 3:
	
	numero1 = input("Introduce un numero para multiplicar: ")
	numero2 = input("Introduce otro numero: ")
	multiplicar = numero1 * numero2
	
	print 'El resultado es: ', multiplicar

if opcion == 4:
	
	numero1 = input("Introduce un numero para dividir: ")
	numero2 = input("Introduce otro numero: ")
	dividir = numero1 / numero2
	
	print 'El resultado es: ', dividir
