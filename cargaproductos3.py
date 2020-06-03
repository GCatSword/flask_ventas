import sqlite3
import csv

fVentas = open('./sales.csv', 'r')
csvreader = csv.reader(fVentas, delimiter=',')

d = {}
for linea in csvreader: 
    if linea[2] not in  d and linea[2] != 'tipo_producto':
         d[linea[2]] = {"precio_unitario":float(linea[9]), "coste_unitario":float(linea[10])}


conn = sqlite3.connect("./data/prueba.db")

c = conn.cursor()

"""# Create table
c.execute('''CREATE TABLE "productos" (
	"tipo_producto"	TEXT NOT NULL UNIQUE,
	"precio_unitario"	REAL NOT NULL,
	"coste_unitario"	INTEGER NOT NULL
)''')""" 

# Insert a row of data
for t_producto, precio_coste in d.items(): 
    c.execute("INSERT INTO productos (tipo_producto, precio_unitario, coste_unitario) VALUES ('{}', '{}', '{}')".format(t_producto, d[t_producto]["precio_unitario"], d[t_producto]["coste_unitario"]))

# CONSULTO LO QUE HAY EN LA BASE DE DATOS, en la segunda vuelta. 
#c.execute("SELECT * FROM productos")
#print (c.fetchall())

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
