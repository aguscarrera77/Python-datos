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

#Limpiar y curar los datos que no estan o estan siendo erroneos.
#rellenar los vacios utilizando la edad promedio.

df['Age']=df['Age'].fillna(promedio_edad)

#Detecte los valores de la columna edad con el tipo float y considero que para mejorar mi analisis lo voy a transformar en entero.

#astype() me permite transformar un tipo valor en otro.

df['Age']=df['Age'].astype(int)

print("\nComo quedo la tabla despues de la limpieza")

espacios_blanco=df['Age'].isnull().sum()

#isnull():chequear celda por celda para ver que contenido tiene. Si celda esta vacia devuelve True que vale 1 y si la celda tiene contenido es False y devuelve 0.

print(f'Cantidad de espacios en blanco en la columna Age es de :{espacios_blanco}')
print('Primeros 5 lugares de la columna Age con datos limpios')

print(df['Age'].head())

promedio_final=df['Age'].mean()
print('El promedio final de edad es :',promedio_final)
print('El promedio antes de limpiar las celdas era: ',promedio_edad)

# LISTA DE MUJERES QUE VIAJABAN EN PRIMERA CLASE Y QUE SOBREVIVIERON PORQUE QUIERE HOMENAJEARLAS.

# 3 CONDICIONES: FEMALE(MUJER),SURVIVED(1),PRIMERA CLASE(1)

mujeres_primera_sobrevivientes=df[
(df['Sex']=='female') &
(df["Survived"]==1)&
(df['Pclass']==1)
]

print(f'Encontramos {len(mujeres_primera_sobrevivientes)} que cumplen los requisitos solicitados por la empresa navia.')

print(mujeres_primera_sobrevivientes[['Name','Age']].head())

#Crear una columna nueva con una condicion.
#Condicion es Menor o adulto. Columna nueva con ese dato.

df['Categoria_Edad']=np.where(df['Age']>18,'Adulto','Menor')

print(df[['Name','Age','Categoria_Edad']].head())

#el metodo groupby() juntar varios registros. Es un equivalente a tablas dinamicas de excel.

#promedio de la tarifa por clase.
#Agrupar por clase 1, 2 , 3. Uso el metodo groupby
#la columna que uso para el calculo es FARE(TARIFA.)
#promedio uso mean.

reporte_tarifas=df.groupby('Pclass')['Fare'].mean()

print('TARIFA PROMEDIO POR CLASE.')
print(reporte_tarifas)