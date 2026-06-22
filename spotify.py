import pandas as pd
import numpy as np

df=pd.read_csv('spotify-2023.csv',encoding='latin-1')

# DIAGNOSTICO.

print('----DIAGNOSTICO------')
print(f'Dimensiones de Dataframe Spotify-2023 {df.shape[0]} filas y {df.shape[1]} columnas')
#953 filas y 24 columnas.

#DATACLEANING. LIMPIEZA DE DATOS.
# VOY A BUSCAR DATOS VACIOS, NULOS O TIPOS DE DATOS ERRONEOS.
#VALORES VACIOS. isna()

vacios_columnas=df.isna().sum()
print('Valores vacios por columna')

print(vacios_columnas[vacios_columnas>0])

#limpiar la columna key

df['key']=df['key'].fillna('Unknown')

#canciones con mas tonalidades en la lista.

ranking_tonalidades=df['key'].value_counts()#cuenta cuanta veces se repite un valor.

print('Tonalidades mas usadas por los musicos en 2023.')
print(ranking_tonalidades)

#contar la cantidad de veces que se escucharon las canciones de este lista.
#necesito limpiar la columna de errores para poder contabilizar de manera correcta las reproducciones.

#df['stream']=df['stream'].astype(int)

#si la columna stream tiene NaN no se convierte a entero.
#necesito otro metodo que me permita usar enteros y NaN sin romper nada.
#errors: coerce caracteres raros o fuera del codigo los transforma en NaN.

df['streams']=pd.to_numeric(df['streams'],errors='coerce')

mediana_streams=df['streams'].median()
df['streams']=df['streams'].fillna(mediana_streams)

print('LIMPIEZA COMPLETA DATOS ACTUALIZADOS. ')