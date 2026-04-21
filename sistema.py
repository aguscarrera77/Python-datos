# Toma parte de la funcion de mi laburo anterior para el usa de agregar personas.


def agregar_personas(personas):
    nombre=input("Cargar nombre")
    edad=int(input('Cargar edad'))

    persona={
        "nombre":nombre,
        "edad":edad
    }
    personas.append(persona)

#Como muestro los datos guardados.

def mostrar_personas(personas):
    for persona in personas:
        print(persona['nombre'] ,'-', persona['edad'])


# promedio de edad. 
# declaro una variable como acumulador.
#dividir por la cantidad de usuarios que se registren.

def promedio(personas):
    suma=0
    for persona in personas:
        suma= suma + persona['edad']
    promedio=suma/len(personas)
    return promedio

# necesito saber mayores y menores a 18.
# 1 recorrer la lista
#2 genero una condicion con if.
# 3 armo dos listas con mayores y menores.

def listas_edades(personas):
    mayores=[]
    menores=[]
    for persona in personas:
        if persona['edad']>=18:
            mayores.append(persona)
        else: menores.append(persona)
    return mayores, menores


#buscar nombre
# generar un input en la funcion donde poner el dato a comparar.
#recorrer la lista
#comparar con la lista.

def buscar_persona(personas):
    nombre_buscado=input("nombre a buscar:")
    for persona in personas:
        if persona["nombre"]== nombre_buscado:
            return persona
    return None

personas=[]

while True:
print("\n1 Agregar personas")
print('2.Mostrar personas')
print("3. Promedio de edades")
print("4.Mayores y Menores")
print('5:Buscar personas')
print("6:SALIR")

opciones=int(('Elegir una opcion'))

if opciones==1:
    agregar_personas(personas)

