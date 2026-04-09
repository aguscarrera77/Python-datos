# for es un bucle que recorre una estructura y me trae los datos. Sintaxis del for: for elemento in bloque
#elemento es la unidad de la estructura.
#bloque es el nombre de la estrutura entera.

for letra in "Python":
    print(letra)

#Ventajas del for: 1- no necesita contador!!!! 2- no tiene condicion. 3- recorre siempre.

numeros=[10,30,45,89]

for numero in numeros:
    print(numero)


# for y metodos.

nombres=['ana','carlos','roberto']


for nombre in nombres:
    print(nombre.title())

# for y if .

enteros=[10,30,10,8,14,40,90]

for e in enteros:
    if e >=18:
        print(e)

for e in enteros:
    if e >=18:
        print("Son mayores a 18 >",e)
    else:print("Son menores a 18 < ",e)

# acumulador y contador.

total=0

for n in [2,15,6]:
    total += n

print(total)

pares=0

for n in [19,10,8,17,21,8]:
    if n % 2==0:
        pares += 1

print(pares)

#for y diccionario.

perfiles={
    'nombre':'Carlos',
    'edad': 25,
    'Trabajo':'Instructor'
    

}

for clave in perfiles.keys():
    print(clave)