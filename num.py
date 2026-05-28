import numpy as np

precios_lista=[100,250,68,90]
precios_iva=[]

for precio in precios_lista:
    precios_iva.append(precio * 1.21)

print(precios_iva)

#Numpy me permite usar estructuras mas rapidas y menos pesadas por ej para calculos matematicos a gran escala.


precios_nplista=np.array([100,250,68,90])#primer array de np. Mantiene homogeneidad de datos.
precios_npiva= precios_nplista * 1.21

print(precios_npiva)
#que pasa cuando no mantengo los valores del mismo tipo.
arreglo_raro=np.array([10,30,4.5])

print(arreglo_raro)

#1 dimension.

dimension_una=np.array([5.5,6.7,10.0,3.8])

#2 dimensiones: columnas y filas. muy usado cuando tenemos base de batos.
#ej: meses: enero/febrero/marzo
dimension_dos=np.array([
[1000,2000,3000], #Vendedor0 
[300,400,5000],#Vendedor1
[500,8000,640]#Vendedor2
])

#dimension3: agregamos otro bloque de datos.
#filas:dias, columnas: cursos(codigo1,codigo2)
dimension_tres=np.array([
[[22,18],[24,19]],
[[34,8],[23,34]]
])
print(dimension_una)
print(dimension_dos)
print(dimension_tres)

#creamos array estructurales.

m_pesos=np.ones((3,5))

print(m_pesos)

#generar id con rangos marcados.

m_rangos=np.arange(100,112)
#generar secuencia de datos. 0 a 24 horas. Cada 6 horas.
m_horario=np.arange(0,24,6)
print(m_rangos)
print(m_horario)

#Dentro del formato filas y columnas buscamos valores especificos. 

# filas pacientes.
#columnas: edad,presion,colesterol

pacientes=np.array([
    [23, 120, 80],#paciente 0
    [87, 135, 900],#paciente 1
    [56,110,76]#paciente 2


])
#quiero saber el colesterol del paciente que tiene edad 87. Dato unico.
paciente_uno=pacientes[1,2]
 
print(paciente_uno)

#Toda columna. todo colesterol.

columna_colesterol=pacientes[:,2]

print(columna_colesterol)

#filas y columnas.Segmentar la matriz.

datos_internos=pacientes[0:1,1:1]

print(datos_internos)