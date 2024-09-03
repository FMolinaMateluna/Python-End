import numpy as np
import pandas as pd
from pandas import DataFrame
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
# Definir la ruta relativa al archivo CSV
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
#Obtenemos el total de casos por cada mes 
casos_enero = df_enero[["Confirmed","Deaths","Recovered"]].sum()
casos_febrero = df_febrero[["Confirmed","Deaths","Recovered"]].sum()
casos_marzo = df_marzo[["Confirmed","Deaths","Recovered"]].sum()
#Creamos un nuevo un DataFrame con los datos totales y un índice de cada mes
df_total = pd.DataFrame({
    "confirmados": [casos_enero["Confirmed"], casos_febrero["Confirmed"], casos_marzo["Confirmed"]],
    "muertes": [casos_enero["Deaths"], casos_febrero["Deaths"], casos_marzo["Deaths"]],
    "recuperados": [casos_enero["Recovered"], casos_febrero["Recovered"], casos_marzo["Recovered"]]
},index=["Enero","Febrero","Marzo"])
print(df_total)
#Creamos el grafico que refleje la evolucion de casos por cada mes
plt.figure(figsize=(10, 6))
plt.plot(df_total.index, df_total["confirmados"], label="Confirmados", marker="o")
plt.plot(df_total.index, df_total["muertes"], label="Muertes", marker="o")
plt.plot(df_total.index, df_total["recuperados"], label="Recuperados", marker="o")
#Definimos las etiquetas y titulos
plt.xlabel("Meses")
plt.ylabel("Número de Casos")
plt.title("Evolución COVID primer trimestre 2021")
plt.legend(title="Tipo de casos", bbox_to_anchor=(1, 1))
#Mostramos el grafico final
plt.show()
