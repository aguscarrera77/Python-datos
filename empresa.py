# CRUD: CREAT READ UPDATE DELETE
import sqlite3

conexion=sqlite3.connect("empleados.db")
cursor=conexion.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS empleados
               (id  INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               puesto TEXT,
               salario REAL,
               fecha_nacimiento DATE)""")

print('1.Tabla creada con exito.')

#INSERTO VALORES.

cursor.execute("""INSERT INTO empleados(nombre,puesto,  salario, fecha_nacimiento) VALUES ("Carlos Gardel","Instructor", 850,"1898-01-01")
""")

#INSERTAR VARIOS DATOS.

nuevos_empleados=[
('Roberto Galan','Secretario',670,'1910-08-12'),
('Gonzalez Rivero','Preceptor',620,'1908-08-08'),
('Nacha Guevera','Directora',890,'1925-10-26'),
('Ana Martinez','Portera',250,'1960-05-10')
]

cursor.executemany("""INSERT INTO empleados(nombre,puesto,salario,fecha_nacimiento)VALUES(?,?,?,?)""",nuevos_empleados)

conexion.commit()# GUARDO LOS DATOS INSERTADOS.
print("2.Datos Insertados correctamente")
#LECTURA DE DATOS.
#fetch all trae varias filas.
#where me permite en la seleccion de datos generar una condicion.
#ORDER BY ORDENA ASC ASCENDENTE Y DESC DESCENDENTE.

cursor.execute("""SELECT nombre,puesto FROM empleados WHERE salario > 620 ORDER BY  salario DESC
""")

for nombre,puesto in cursor.fetchall():
    print(f"{nombre}-{puesto}")

#UPDATE edita datos de la tabla.

# voy a aumentar el sueldo de carlitos gardel 200.

nuevo_sueldo=1050
nombre_empleado="Carlos Gardel"

cursor.execute("""UPDATE empleados SET salario=? WHERE nombre=?""",(nuevo_sueldo,nombre_empleado))
conexion.commit()

print(f"Nuevo salario de {nombre_empleado} : {nuevo_sueldo}")

#DELETE borra datos.

#despedimos a nacha guevera por carpeta psiquiatrica.

eliminar_id= 4 #elimina datos buscando el id.

cursor.execute("""DELETE FROM empleados WHERE id=?
""",(eliminar_id,))

conexion.commit()
print("Empleado con id: ",eliminar_id,"despedido")

print("Estado final de la tabla empleados" )

cursor.execute("SELECT id,nombre,salario FROM empleados")

for empleado in cursor.fetchall():
    print(f"ID:{empleado[0]},Nombre: {empleado[1]},Salario: {empleado[2]}")

conexion.close()



