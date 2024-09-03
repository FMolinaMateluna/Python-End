# Importamos Numpy
import numpy as np
# Definimos un array de 4 dimensiones
array_base = np.random.randint(1, 5, size=(2, 2, 3,4))
# Comprobamos que tiene cuatro dimensiones
if array_base.ndim == 4:
    print("El array tiene 4 dimensiones")
else:
    print("No es un array de 4 dimensiones")
# Mostramos las dimensiones y el tipo de contenido
print (array_base.shape , array_base.dtype)
# Calculamos la suma del array en funcion de sus ultimos dos ejes
suma = np.sum(array_base, axis=(2, 3))
# Mostramos en pantalla el resultado de la suma
print(suma)