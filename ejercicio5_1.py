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
# Mostramos la informacion del dataFrame
print("Información del DataFrame:")
print(df_enero.info())
# Sumamos los datos faltantes por cada columna de nuestro DataFrame
datos_faltantes = df_enero.isna().sum()
# Mostramos por pantalla el total de datos faltantes por columna
print("Datos Faltantes:")
print(datos_faltantes)
# Mostramos por pantalla las primeras 5 filas.
print("Primeras 5 filas:")
print (df_enero.head())