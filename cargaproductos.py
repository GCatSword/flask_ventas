import sqlite3
import csv



fVentas = open('./sales10.csv', 'r')
csvreader = csv.reader(fVentas, delimiter=',')

conn = sqlite3.connect("./data/prueba.db")
c = conn.cursor()

registros=[]

for linea in csvreader:
    registros.append(linea)

#print(len(registros))
del registros[0]   
#print(registros)



for linea in registros:
    p = [linea[2], float(linea[9]), float(linea[10])]
    print(p)
    try:
        #print(d)
        c.execute("INSERT INTO productos (tipo_producto, precio_unitario, coste_unitario) VALUES (?,?,?)", (p))
    except sqlite3.Error:
        #print(d)
        pass
    
#print(d)

#c.execute("INSERT INTO productos (tipo_producto, precio_unitario, coste_unitario) VALUES (?,?,?)", (p))

conn.commit()
c.close()
conn.close()
