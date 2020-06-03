import sqlite3
import csv

filename = "./sales.csv"
database = "./data/ventas.db"

fSales = open(filename, 'r')
csvreader = csv.reader(fSales, delimiter=',')

conn = sqlite3.connect(database)
cur = conn.cursor()

headerRow = next(csvreader)

query = ("INSERT OR IGNORE INTO productos(tipo_producto, precio_unitario, coste_unitario) VALUES (?,?,?)")

for dataRow in csvreader:
    tupla_datos = ( dataRow[2], float(dataRow[9]), float(dataRow[10]) )
    cur.execute(query, tupla_datos)



conn.commit()
cur.close()
conn.close()
