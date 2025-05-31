#Clase:        Clase 6
#Tema:         Manejo de lista
#Ejercicio:    6.3.1 Numeros lideres
#Descripción:  Un programa donde si un numero en una lista es lider es estrictament mayor que todos los elementos a su derecha dada una lista implementada por el usuario imprime todos los numeros lideres. 
#Fecha:        2025-05-30
#Estado:       [ Terminado ]
lista = input("Ingresa una lista de números: ").split()

lista1 = [int(num) for num in lista]

lideres = []

for i in range(len(lista)):
    numerolider = True
    for j in range(i + 1, len(lista)):
        if lista[i] <= lista[j]:
            numerolider = False
            break
    if numerolider:
        lideres.append(lista[i])

print("Números líderes:", lideres)