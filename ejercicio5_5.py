# Importamos las librerias necesarias 
import numpy as np
import pandas as pd
from pandas import DataFrame
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
# Definir la ruta relativa al archivo CSV
RUTA_RELATIVA = os.path.join(".", 'Data')
csv_file = os.path.join(RUTA_RELATIVA, 'COVID_01-01-2021.csv')
# Leer el archivo CSV usando la ruta relativa
datos_enero = pd.read_csv(csv_file, sep=",")
# Convertir los datos a un DataFrame
df_enero = DataFrame(datos_enero)
# Sumamos los casos totales por pais
casos_paises=df_enero.groupby("Country_Region").agg({
    "Confirmed": "sum",
    "Deaths": "sum",
    "Recovered": "sum"
})
# Filtramos los paises que tengan mas de 150 muertes
mas_casos = casos_paises.groupby("Country_Region").filter(lambda x: x["Deaths"].mean() < 150)
# Creamos una tabla pivote para reorganizar los datos
df_pivot = mas_casos.pivot_table(values=["Confirmed", "Deaths", "Recovered"], index="Country_Region", aggfunc="sum")
# Preparamos los datos para el gráfico
categorias = df_pivot.index 
confirmed = df_pivot["Confirmed"].values
deaths = df_pivot["Deaths"].values
recovered = df_pivot["Recovered"].values
# Configuración de la posición de las barras
x = np.arange(len(categorias))  # Rango para el eje x
ancho = 0.2  # Ancho de las barras
# Creamos el grafico
fig, ax = plt.subplots(figsize=(80, 40))
barras1 = ax.bar(x - ancho, confirmed, ancho, label="Confirmed")
barras2 = ax.bar(x, deaths, ancho, label="Deaths")
barras3 = ax.bar(x + ancho, recovered, ancho, label="Recovered")
# Definicion de etiquetas, título y leyenda
ax.set_xlabel("PAISES")
ax.set_ylabel("CASOS")
ax.set_title("Grafico total de casos en paises con menos de 150 muertes")
ax.set_xticks(x)
ax.set_xticklabels(categorias, rotation=90)
ax.legend()
# Mostramos el gráfico
plt.show()
