#Clase:        Clase 5
#Tema:         Manejo de lista
#Ejercicio:    5.4.2  Suma de valores posicionales 
#Descripción:  Pide al usuario un solo numero u suma sus valores hasta que quede ese numero
#Autor:        Fabiola Guardado
#Fecha:        2025-05-30
#Estado:       [ Terminado ]

numero = int(input("Ingresa un número: "))

while numero >= 10:
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    numero = suma

print("El resultado es:", numero)