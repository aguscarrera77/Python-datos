#while: bucle que repite contenido si la condicion es true.
#sintaxis: while condicion: 
#            contenido
#          contador(permite que el bucle sume unidades a la variable de inicio.)

numero=5
while numero>=0:
    print(numero)
    numero=numero - 2

suma=0

while suma<=20:
    suma= suma + 3
    print("La suma controlada: ",suma)


#strings: vamos a recorrer una palabra con while.

saludo="hola como estan?"

i=0

while i < len(saludo):
    print(saludo[i])
    i= i + 1

palabra="neuquen"
i= len(palabra)-1 #porque necesito que cuente desde la ultima posicion.

while i >= 0:
    print(palabra[i])
    i= i - 1

mensaje= 'Bienvenido'
contador=0
#quiero que le de la bienvenida 3 veces.

while contador < 3:
    print(mensaje)
    contador= contador + 1

# while+ if: while controlar la repeticion. if decide que accion se toma.
# vamos a buscar numeros pares de un conjunto de numeros.

contador=1
while contador<=20:
    if contador %2==0:
        print("Es numero par: ",contador)
    else:print("Es numero impar: ",contador)
    contador=contador + 1

# la condicion del if es resto de 0 entonces es par.

#while + metodos:

texto=" miercoles "
contador=0

while contador <=2:
    print(texto.strip().upper())
    contador= contador + 1

#while + if + metodos.

frase= "javascript"
contador=1

while contador <=4:
    if contador % 2==0:
        print(frase.upper())
    else:print(frase.title())
    contador= contador + 1

# recorrer variables con varios valores y sabe cuanto va a iterar.

# Sumar ingresos.

ingresos=[10,30,35,40,56]

i=0
total=0

while i < len(ingresos):
    total= total + ingresos[i]
    i= i + 1
print('Mi sueldo en dolares: ',total)

#recorro una lista y trato de encontrar un valor.

productos=[100,200,300,400,500,600]

i=0

while i < len(productos) and productos[i] != 300:
    i= i + 1
print('La posicion de 300 es: ',i)



    
