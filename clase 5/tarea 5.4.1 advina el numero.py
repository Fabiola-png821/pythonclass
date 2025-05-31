#Clase:        Clase 5
#Tema:         Bucles for y while
#Ejercicio:    5.4.1  Adivina el numero
#Descripción:  Genera un numero aleatorio entre 1 y 100 y pide al usuario que lo adivine 
#Autor:        Fabiola Guardado
#Fecha:        2025-05-30
#Estado:       [ Terminado ]

import random
numerosecreto = random.randint(1, 100)
numero= 0

while numero != numerosecreto:
    numero= int(input("Adivina el numero 1-100: "))
    if numero < numerosecreto:
        print("El numero secreto es mayor")
    elif numero > numerosecreto:
        print("El numero secreto es menor:")
    else:
        print("Felicidades adivinaste el numero. Fin del juego")
