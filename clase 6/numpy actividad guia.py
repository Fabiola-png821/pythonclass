import numpy as np
mylist =[1, 2, 3, 4, 5]
arr= np.array(mylist)
print(arr)

zeros =np.zeros(5)
print(zeros)

ones= np.ones(5)
print(ones)

arr1= np.array([1,2,3])
arr2= np.array([4,5,6])
resultado = arr1 + arr2 
resultado= arr1 * arr2 

arr = np.array([1, 2, 3])
result = arr + 5

arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
result = arr1 + arr2

arr = np.array([1, 2, 3, 4, 5])
slice = arr[1:4]

# Indexación booleana
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
result = arr[mask]

arr = np.array([1, 2, 3, 4, 5])
indices = np.array([0, 2, 4])
result = arr[indices] 

#Concatenación
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))

#División
arr = np.array([1, 2, 3, 4, 5, 6])
split = np.split(arr, 3) 

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

print("Dimensiones", consumo.ndim)
print("Forma:", consumo.shape)
print("Tipo de datos:", consumo.dtype)
print("consumo primer hogar", consumo[0])
print("consumo de dia miercoles(dia3)", consumo[:,2])

#Calculo de promedio de hogares 
promedioporhogar=np.mean(consumo, axis=1)
#Promedio de consumo diario de todos los hogares
promediopordia= np.mean(consumo, axis=0)
#Suma total de consumo en la semana de los 10 hogares 
totalconsumo=np.sum(consumo)

#Maximo por hogar 
maximos= np.max(consumo, axis=1)
#Minimo por dia 
minimos= np.min(consumo, axis=0)
#Desviacion estandar global 
desviacion= np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

#Suma por hogar 
consumototalhogar= np.sum(consumo, axis=1)
#Indice del hogar con mayor consumo 
hogarmayorconsumo= np.argmax(consumototalhogar)
#Indice del hogar con mejor consumo
hogarmaseficiente= np.argmi(consumototalhogar)

print(consumototalhogar)
print(hogarmayorconsumo)
print(hogarmaseficiente)

#Suma por hogar(semana)
consumototalhogar=np.sum(consumo, axis=1)
print(f"Consumo total de cada hogar durante:{consumototalhogar}")
#Compra cada hogar con una valor mayor a 100
altos= consumototalhogar >100 
#Filtrando hogares que cumplen la condicion: 
consumomayor100= np.where(altos)[0]
print(f"ids de hogares con consumo mayor a 100: {consumomayor100}")

#Aplicando normalizacion MinMax al conjunto de datos
consumonormalizado=(consumo - consumo.min()) / (consumo.max() -consumo.min())
#Resultado 
print(consumonormalizado)


