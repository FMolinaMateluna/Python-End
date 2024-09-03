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
#Agrupamos las provincias sumando el caso de recuperados de cada una
total_provincias = df_enero.groupby(["Country_Region", "Province_State"]).agg({
    "Recovered": "sum"
}).reset_index()
#Filtramos solo las provincias que no tienen recuperados
no_recuperados = total_provincias[total_provincias["Recovered"] == 0]
#Obtenemos por el indice de Provincias, el pais y los recuperados
paises = no_recuperados.set_index("Province_State")[["Country_Region","Recovered"]]
#Mostramos por pantalla los resultados
print("Provincias sin pacientes recuperados:")
print(paises)