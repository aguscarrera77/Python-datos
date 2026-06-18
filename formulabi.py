


import numpy as np
import pandas as pd



# Creamos la matriz de la academia de pilotos
pilotos = np.array([
    [10, 290, 2],  # Piloto 10
    [11, 310, 0],  # Piloto 11
    [12, 280, 5],  # Piloto 12
    [13, 300, 2]   # Piloto 13
])

print("--- TABLA INICIAL DE PILOTOS ---")
print(pilotos)
# El nuevo piloto tiene: ID 14, Velocidad 305, Penalizaciones 1
# ¡Ojo! Se pasa como una lista de listas [[...]] para que NumPy entienda que es una FILA.
nuevo_piloto = np.array([[14, 305, 1]])

# Los fusionamos verticalmente
pilotos_actualizados = np.vstack((pilotos, nuevo_piloto))

print("--- DESPUÉS DE VSTACK (Nuevo piloto abajo) ---")
print(pilotos_actualizados)

# Años de experiencia para los 5 pilotos actuales (en orden del 10 al 14)
# Lo creamos como columna vertical usando doble corchete
experiencia = np.array([[3], [5], [1], [4], [2]])

# Los fusionamos horizontalmente
dataset_completo = np.hstack((pilotos_actualizados, experiencia))

print("--- DESPUÉS DE HSTACK (Nueva columna de experiencia al costado) ---")
print(dataset_completo)
# Ahora las columnas son: [ID, Velocidad, Penalizaciones, Experiencia]
# Recibimos una lista plana (1D) con los puntajes de la carrera
puntajes_planos = np.array([80, 95, 40, 85, 90])
print("Forma original:", puntajes_planos.shape) # Salida: (5,)
# Transmutación a un vector columna vertical (5 filas, 1 columna)
# El truco del -1 le pide a NumPy calcular automáticamente las filas
puntajes_verticales = puntajes_planos.reshape(-1, 1)
print("Nueva forma:", puntajes_verticales.shape) # Salida: (5, 1)
print("--- PUNTAJES TRANSFORMADOS A VECTOR COLUMNA ---")
print(puntajes_verticales) 

# --- ASÍ LO HACEMOS HOY EN NUMPY (Filosofía de Matriz Pura) ---
# Si quiero las velocidades, tengo que recordar que es la columna índice 1
velocidades_numpy = dataset_completo[:, 1]
print("Velocidades con NumPy (Cálculo directo en memoria):", velocidades_numpy)

#Vamos a empezar a trabajar con panda.Con datos que ya teniamos.


df=pd.DataFrame(dataset_completo,columns=['ID','Velocidad','Penalizacion','Experiencia'])

print(df)

print('\nVelocidades de mi nueva data frame')
print(df['Velocidad'])

filas,columnas=df.shape

print(filas,columnas)