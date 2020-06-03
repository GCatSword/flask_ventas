import sqlite3
import csv

import time
start_time = time.time()

fVentas = open('./sales.csv', 'r')
csvreader = csv.reader(fVentas, delimiter=',')

conn = sqlite3.connect("./data/prueba.db") #db de prueba, canviar por la original cuando esté bién.
c = conn.cursor()

registros=[]
d = {}

for linea in csvreader:
    registros.append(linea)

#print(len(registros))
del registros[0] #borrar linea inicial, para evitar problemas con float.
#print(registros)

lst_productos=[]
'''
for linea in registros:
    lst_productos += [linea[2], float(linea[9]), float(linea[10])]
'''

for linea in registros:
    lst_productos += [linea[2], float(linea[9]), float(linea[10])]
    '''try:
        c.execute("INSERT INTO productos (tipo_producto, precio_unitario, coste_unitario) VALUES (?,?,?)", (lst_productos))
    except sqlite3.Error:
        pass
    '''

# lst_productos = lista con todos los elementos del documento csv menos la 1a linea.

# a =[acumulador[x:x+3] for x in range(0, len(acumulador), 3)]
# expresión sacada de internet, creo entender el funcionamiento. modifico, para entender mejor.

sub_lst=[]
for x in range(0, len(lst_productos), 3):# Crear sub-listas cada 3 elementos.
    sub_lst += [lst_productos[x:x+3]]

'''
#Solución que dio Ramón en clase, dijo que un poco bruta. Intentar sacar otra solución.
for p in sub_lst:
    try:
        c.execute("INSERT INTO productos (tipo_producto, precio_unitario, coste_unitario) VALUES (?,?,?)", (p))
    except sqlite3.Error:
        pass
'''

# Con el REPLACE evitamos el problema si ya existe, pero no creo que sea la solución óptima.
# problema con esto: al reemplazar uno existente, la ID del inicial desaparece y se sustituye por la ID del REPLACE.
for p in sub_lst:
    #print(p)
    #c.execute("INSERT OR REPLACE INTO productos (tipo_producto, precio_unitario, coste_unitario) VALUES (?,?,?)", (p))
    c.execute("INSERT OR IGNORE INTO productos(tipo_producto, precio_unitario, coste_unitario) VALUES (?,?,?)", (p))
    c.execute("DELETE FROM sqlite_sequence WHERE name='productos'")
# IGNORE tampoco evitamos el cambio de id, cuando "ignora" salta al siguiente id.
# Solucionado problema id con borrar el contador del autoincremento del id.

conn.commit()
c.close()
conn.close()

print("--- %s seconds ---" % (time.time() - start_time))