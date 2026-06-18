import pandas as pd
import numpy as np
#Pimero llamo al archivo y lo traigo a mi archivo py.
df=pd.read_csv('titanic.csv')

#head: es para chequear las primeras filas y columnas  del archivo.

print(df.head())
#cuantas filas y cuantas columnas. Metodo shape.
print(f'\n Data frame {df.shape[0]} filas y {df.shape[1]} columnas')

#info() que me determina que tipo valores tienen las estructuras.

print('\n Radiografia datos.')
df.info()

#seleccionar y filtrar.
#Voy a seleccionar una columna.

names=df["Name"]
print(names.head())


#Filas: quiero ver lista sobrevivientes. Aclaracion en la columna Survived SI=1 y NO=0.

sobrevivientes=df[df['Survived']==1]

print(f"\nCantidad de sobrevivientes: {len(sobrevivientes)}")
#NOMBRE Y EDAD.

print(sobrevivientes[['Name','Age']].head())

#FILTRAR PASAJEROS EN TERCERA CLASE.

#llamar a la columna que tenga los datos de las clases.

condicion=df['Pclass']==3

pasajeros_tercera=df[condicion]

print('\n Listas de pasajeros de tercera clase')
#quiero saber el nombre y que figure la Pclass.
print(pasajeros_tercera[['Name','Pclass']].head())

#quiero saber cuantos pasajeros tienen mas de 60 anos.

mayores_60=df[df['Age']>60]

cantidad_mayores=len(mayores_60)

print(cantidad_mayores)

#quiero cuantas mujeres viajaban en primera clase.
#2 condiciones diferentes el sexo y que viajaban en primera clase

condicion_mujer=df['Sex']=='female'
condicion_clase=df['Pclass']==1

mujeres_primera=df[condicion_mujer & condicion_clase]

print(f' Se encontraron {len(mujeres_primera)} pasajeras.')
#DATACLEAN.. EN ESTA CASO PODEMOS VER O QUE EXISTEN QUE NO FUERON COMPLETADOS O QUE CON EL CORRER TIEMPO ESOS DATOS SE PERDIERON.

#SI EN LA COLUMNA EDAD EXISTAN CELDAS VACIOS O DATOS ERRONEOS(NaN)

edad_vacia=df['Age'].isna().sum()

print('Las celdas que estan vacias: ',edad_vacia)

#promedio de edad.

promedio_edad=df['Age'].mean()

print(promedio_edad)