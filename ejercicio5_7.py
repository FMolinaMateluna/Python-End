#Importamos las librerias necesarias
import numpy as np
import pandas as pd
import os
from pandas import DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt
#Definimos la ruta relativa al archivo CSV
RUTA_RELATIVA = os.path.join(".", 'Data')
csv_enero = os.path.join(RUTA_RELATIVA, 'COVID_01-01-2021.csv')
csv_febrero = os.path.join(RUTA_RELATIVA, 'COVID_01-02-2021.csv')
csv_marzo = os.path.join(RUTA_RELATIVA, 'COVID_01-03-2021.csv')
#Leemos los datos de los ficheros con formato csv
datos_enero = pd.read_csv(csv_enero, sep=",")
datos_febrero = pd.read_csv(csv_febrero, sep=",")
datos_marzo= pd.read_csv(csv_marzo, sep=",")
#Convertimos dichos datos a un DataFrame
df_enero = DataFrame(datos_enero)
df_febrero= DataFrame(datos_febrero)
df_marzo= DataFrame(datos_marzo)
'''Desde los dataFrame mensuales, seleccionamos los datos que necesitamos para el uso de nuestro grafico,
teniendo en cuenta que solo vamos a utilizar las provincias del pais de España'''
datos_necesarios = ["Province_State", "Confirmed", "Recovered"]
df_españa_enero = datos_enero[datos_enero["Country_Region"] == "Spain"][datos_necesarios]
df_españa_febrero = datos_febrero[datos_febrero["Country_Region"] == "Spain"][datos_necesarios]
df_españa_marzo = datos_marzo[datos_marzo["Country_Region"] == "Spain"][datos_necesarios]
#Añadimos una columna con el mes
df_españa_enero['Mes'] = 'Enero'
df_españa_febrero['Mes'] = 'Febrero'
df_españa_marzo['Mes'] = 'Marzo'
'''Unimos los dataframe que teniamos por meses y los colocamos en uno que muestre la totalidad de los casos confirmados y 
recuperados, eliminando la fila que no tiene datos definidos'''
df_españa = pd.concat([df_españa_enero, df_españa_febrero, df_españa_marzo])
df_españa_confirmados = df_españa[df_españa["Confirmed"]!=0]
'''Mostramos en pantalla los datos para asegurarnos que estan todos segun lo solicitado'''
print(df_españa_confirmados)
#Creamos el gráfico para casos confirmados
plt.figure(figsize=(10, 8))
#Obtenemos una lista única de provincias
provincias = df_españa_confirmados['Province_State'].unique()
#Dibujamos una línea por cada provincia de España con los casos confirmados
for provincia in provincias:
    df_provincia = df_españa_confirmados[df_españa_confirmados['Province_State'] == provincia]
    plt.plot(df_provincia['Mes'], df_provincia['Confirmed'], marker='o', label=provincia)
#Titulo del grafico y sus ejes
plt.title("Casos confirmados por provincia en España. 1er Trimestre")
plt.xlabel("Meses")
plt.ylabel("Casos Confirmados")
plt.legend()
#Definimos la leyenda y su caracteristica
plt.legend(title="Provincias Españolas", bbox_to_anchor=(1, 1))
#Mostramos el gráfico para confirmados
plt.show()
#Creamos el gráfico para casos recuperados y sus variables, dibujando una linea por cada provincia
plt.figure(figsize=(10, 8))
for provincia in provincias:
    df_provincia = df_españa_confirmados[df_españa_confirmados['Province_State'] == provincia]
    plt.plot(df_provincia['Mes'], df_provincia["Recovered"], marker='o', label=provincia)
#Titulo del grafico y sus ejes
plt.title("Recuperados por provincia en España. 1er Trimestre")
plt.xlabel("Meses")
plt.ylabel("Casos Recuperados")
plt.legend()
#Definimos la leyenda y su caracteristica
plt.legend(title="Provincias Españolas", bbox_to_anchor=(1, 1))
#Mostramos el gráfico para recuperados
plt.show()