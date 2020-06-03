from the_app import app
from flask import Flask, render_template, request, redirect, url_for
import csv, sqlite3
from the_app.forms import ProductForm

database = "./data/ventas.db"

@app.route("/")
def index():
    fVentas = open('./sales.csv', 'r')
    csvreader = csv.reader(fVentas, delimiter=',')

    registros = []
    d = {}
    for linea in csvreader:
        registros.append(linea)
        if linea[0] in d:
            d[linea[0]]['ingresos'] += float(linea[11])
            d[linea[0]]['beneficios'] += float(linea[13])
        else:     
            if linea[0] != 'region':
                d[linea[0]] = {'ingresos': float(linea[11]), 'beneficios': float(linea[13])}
    
    return render_template('region.html', ventas=d)

@app.route("/paises")
def paises():
    region_name = request.values['region']
    fVentas = open('./sales.csv', 'r')
    csvreader = csv.reader(fVentas, delimiter=',')

    d = {}

    for linea in csvreader:
        if linea[0] == region_name:
            if linea[1] in d:
                d[linea[1]]['ingresos'] += float(linea[11])
                d[linea[1]]['beneficios'] += float(linea[13])
            else:     
                d[linea[1]] = {'ingresos': float(linea[11]), 'beneficios': float(linea[13])}

    return render_template('paises.html', ventas_pais=d, region_nm=request.values['region'])

@app.route("/productos")
def productos():
    conn = sqlite3.connect(database)
    cur = conn.cursor()

    query = "SELECT id, tipo_producto, precio_unitario, coste_unitario FROM productos"
    productos = cur.execute(query).fetchall()

    conn.close()
    return render_template('productos.html', productos=productos)

@app.route("/addproduct", methods=['GET', 'POST'])
def addproduct():
    form = ProductForm()
    
    if request.method == 'GET':
        return render_template('newproduct.html', form=form)
    else:
        conn = sqlite3.connect(database)
        cur = conn.cursor()

        query = "INSERT INTO productos (tipo_producto, precio_unitario, coste_unitario) values (?,?,?); "
        datos = (request.values.get('tipo_producto'), request.values.get('precio_unitario'), request.values.get('coste_unitario'))

        cur.execute(query, datos)

        conn.commit()
        conn.close()

        return redirect(url_for("productos"))





