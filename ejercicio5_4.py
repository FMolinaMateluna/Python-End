# Importamos la libreria pandas y desde esta importamos para utilizar DataFrame
import pandas as pd
from pandas import DataFrame
import os
# Definir la ruta relativa al archivo CSV
RUTA_RELATIVA = os.path.join(".", 'Data')
csv_file = os.path.join(RUTA_RELATIVA, 'COVID_01-01-2021.csv')
# Leer el archivo CSV usando la ruta relativa
datos_enero = pd.read_csv(csv_file, sep=",")
# Convertir los datos a un DataFrame
df_enero = DataFrame(datos_enero)
'''Agrupamos y sumamos las estadisticas de cada pais sumando sus casos confirmados, muertes y recuperados
para que nos devuelva en una sola fila el total de cada pais'''
casos_paises = df_enero.groupby(["Country_Region"]).agg({
    "Confirmed": "sum",
    "Deaths": "sum",
    "Recovered": "sum"
})
'''Con el resultado obtenido por paises, ordenamos el dataframe por la columna de confirmados, de manera descendente
para obtener los paises con mas casos y luego solo seleccionamos los 10 primeros'''
top_paises = casos_paises.sort_values(by='Confirmed', ascending=False).head(10)
#Devolvemos los paises con mas casos
print("Paises con mas casos:")
print(top_paises)