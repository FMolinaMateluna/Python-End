# Importamos Numpy
import numpy as np
# Definimos primero que tipo de dato recibe cada columna
dtype = np.dtype([('Nombre', 'U10'),("Diseño","int"),("Lenguaje","int"),("Base_datos","int"),("Programacion","int")])
'''Creamos una estructura de datos desde la tabla, convirtiendola en un array de una sola dimension y definiendo el 
nombre de cada campo y como esta estructurado cada dato'''
tabla = np.array([("Francisco",9,4,8,3),
                  ("Lucía",7,8,10,5),
                  ("Juan",10,8,6,8),
                  ("Paula",7,4,8,4),
                  ("Alba",8,5,6,5)],dtype=dtype)
# Mostramos la tabla en pantalla
print (tabla)
''' Creamos una funcion para calcular cuantos alumnos han desaprobado por materia. Solo vamos a utilizar los campos que 
tienen numeros para poder comparar si es mayor o no a 5 '''
def mostrar_suspensos(array, excluir_campo=['Nombre']): #Excluimos el campo "Nombres"
    nota = {}
    for campo in array.dtype.names:
        if campo not in excluir_campo:
            nota[campo] = np.sum(array[campo]<5)
    return nota
# Hacemos uso de la funcion para mostrar el total de alumnos que suspendieron por materia
total_suspensos = mostrar_suspensos(tabla)
for campo, suma in total_suspensos.items():
    print(f"Total de alumnos no aprobados en {campo}: {suma}")
# Creamos una funcion para calcular la nota media de cada alumno 
def nota_media(alumno):
    notas_medias = np.array([alumno["Diseño"], alumno["Lenguaje"], alumno["Base_datos"], alumno["Programacion"]])
    return np.mean(notas_medias)
# Hacemos uso de la función para mostrar el nombre del alumno y su nota media obtenida
for alumno in tabla:
    media = nota_media(alumno)
    print(f"{alumno['Nombre']} ha obtenido una nota media de: {media:.2f}")         
# Creamos una funcion para calcular los alumnos que han aprobado y los que no aprobaron el curso
nota_aprobar = 5 #Definimos la nota para aprobar
def calcular_aprobados():
    aprobados = []
    no_aprobados = []
    for alum in tabla:
        notas = np.array([alum["Diseño"], alum["Lenguaje"], alum["Base_datos"], alum["Programacion"]])
        media = nota_media(alum)
        todas_aprobadas = (notas >= nota_aprobar).all()
# Mediante una condicional definimos que para aprobar debe tener todas las materias aprobadas y con una media mayor a 5
        if media >= nota_aprobar and todas_aprobadas:
            aprobados.append(alum["Nombre"])
        else:
            no_aprobados.append(alum["Nombre"])
    if aprobados:
        print (f"Los alumnos que aprobaron el curso son: {', '.join(aprobados)}")
    if no_aprobados:
        print(f"Los alumnos que no aprobaron el curso son: {', '.join(no_aprobados)}")
# Llamamos a la funcion para que nos devuelva los datos requeridos
calcular_aprobados()
           





