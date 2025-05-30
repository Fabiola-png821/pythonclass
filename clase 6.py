#Clase:        Clase 6
#Tema:         Manejo de lista
#Ejercicio:    6.2.1 Eliminando valores duplicados 
#Descripción:  Un programa que dada una lista ingresada por el usuarui elimina los elementos duplicados manteniendo la primera aparicion de cada numero
#Fecha:        2025-05-16
#Estado:       [ Terminado ]

lista =input("Ingresa una lista de números: "). split()
lista1 = [int(num) for num in lista]

listasinduplicados = []

for numero in lista1:
    if numero not in listasinduplicados:
        listasinduplicados.append(numero)

print("Lista sin duplicados:", listasinduplicados)
