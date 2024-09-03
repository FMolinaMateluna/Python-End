# Importamos las librerias random, numpy y pandas para su uso en el programa
import random 
import numpy as np
import pandas as pd
# Creamos una lista con 10 numeros aleatorios entre 0 y 20
serie_lista = [random.randint(0,20) for x in range(10)]
# Convertimos la lista obtenida a serie Pandas y la mostramos en pantalla
serie_A = pd.Series(serie_lista)
print("Serie A:")
print (serie_A)
# Creamos un array con 10 numeros aleatorios entre el 0 y el 20
serie_array = np.random.randint (0,21, size=10)
# Convertimos el array en una serie Pandas y lo mostramos en pantalla
serie_B = pd.Series(serie_array)
print("Serie B:")
print(serie_B)
# Definimos una funcion que retorne el indice de los multiplos de 3 en una serie
def encontrar_posicion (serie):
    return serie[(serie % 3 == 0) & (serie != 0)].index.tolist()
# Invocamos la funcion para buscar los multiplos de 3 en la serie A
multiplos_3 = encontrar_posicion(serie_A)
# Mostramos el resultado
print ("Indice de numeros multiplos de 3 en serie A:",multiplos_3)
# Creamos una funcion para encontrar numeros iguales entre dos series
def encontrar_comunes (serie_1 , serie_2):
    comunes = set(serie_1) & set(serie_2)
    return list(comunes)
# Invocamos la funcion para encontrar los numeros iguales en la serie A y B y mostramos cuales son 
iguales = encontrar_comunes(serie_A, serie_B)
print("Numeros comunes en ambas series:",iguales)
# Creamos una funcion para encontrar numeros unicos entre dos series
def encontrar_unicos (serie_x , serie_y):
    a = set(serie_x)
    b = set (serie_y)
    diferentes_x = a - b
    diferentes_y = b - a
    diferentes = diferentes_x.union(diferentes_y)
    return list(diferentes)
# Invocamos la funcion para encontrar los numeros unicos en la serie A y B y mostramos cuales son 
unicos = encontrar_unicos(serie_A, serie_B)
print("Los numeros unicos entre series son:",unicos)
# Convertimos ambas listas en un DataFrame y lo mostramos
combinadas = pd.DataFrame({"Serie A":serie_A, "Serie B":serie_B})
# Asignamos nombre al indice
combinadas.index.name = 'Índice'
# Mostramos el DataFrame
print ("DataFrame")
print (combinadas)
# Generamos una nueva serie en un DataFrame de 7 filas y 5 columnas
serieC = pd.Series(np.random.randint(1, 10, 35))
# Definimos las filas y columnas 
data_serie = pd.DataFrame(serieC.values.reshape(7, 5))
print("Nuevo DataFrame")
print(data_serie)