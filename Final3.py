# Importamos la librerias necesarias
import numpy as np
import random
# Creamos una variable con numero aleatoreos de vectores
ale_vectores = random.randint(1,5)
vectores =[]
for x in range(ale_vectores):
    longitud = random.randint(1,10) # Definimos la longitud aleatorea
    contenido = np.random.randint (0,200, size = longitud) # Definimos el contenido aleatoreo
    vectores.append(contenido)
# Mostramos la cantidad y el vector o vectores obtenidos
print(f"Número de vectores: {ale_vectores}")
print("Vectores generados:")
for i, vector in enumerate(vectores):
    print(f"Vector {i+1}: {vector}")
# Creamos una funcion que defina el producto cartesiano entre los vectores generados
def producto_cartesiano(vectores):
    if not vectores:
        return [[]]
    resultado = []
    for item in vectores[0]:
        for prod in producto_cartesiano(vectores[1:]):
            resultado.append([item] + prod)
    return resultado
producto_cartesiano_resultado = producto_cartesiano(vectores)
# Mostrar el resultado del producto cartesiano
print("Producto cartesiano de los vectores generados:")
for resultado in producto_cartesiano_resultado:
    print(resultado)
