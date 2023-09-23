import psycopg2

# Establecer la conexión
conexion = psycopg2.connect(host="localhost",
                            database="inventario",
                            user="postgres",
                            password="456jenifer456a")

# Crear un cursor
cursor = conexion.cursor()

# Ejecutar una consulta para obtener los datos de la tabla producto
cursor.execute("SELECT * FROM producto")

# Recorrer los datos obtenidos
for fila in cursor:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()

                            
                            

