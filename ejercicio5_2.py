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
# Obtenemos el total de casos confirmados, fallecidos, recuperados y activos.
casos_paises=df_enero.groupby("Country_Region").agg({
    "Confirmed": "sum",
    "Deaths": "sum",
    "Recovered": "sum",
    "Active": "sum"
})
# Mostramos en pantalla
print("Total de casos por paises:")
print(casos_paises)