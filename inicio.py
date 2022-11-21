from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template("index.html")

@app.route('/participantes')
def participantes():
    return render_template("participantes.html")

@app.route('/servicios')
def servicios():
    return render_template("servicios.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/crud')
def crud():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='Apolo' )
    cursor = conn.cursor()
    cursor.execute('select * from registro order by id')
    datos = cursor.fetchall()
    return render_template("crud.html", comentario = datos)

@app.route('/editar/<string:id>')
def editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='Apolo', port=3306 )
    cursor = conn.cursor()
    cursor.execute('select id, nom, apellido, edad, correo, tel, direc from registro where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editar.html", dat=dato[0])

@app.route('/editar_comenta/<string:id>',methods=['POST'])
def editar_comenta(id):
    if request.method == 'POST':
        n=request.form['nom']
        a=request.form['apellido']
        s=request.form['edad']
        c=request.form['correo']
        t=request.form['tel']
        d=request.form['direc']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='Apolo', port=3306 )
        cursor = conn.cursor()
        cursor.execute('update registro set nom=%s, apellido=%s, edad=%s, correo=%s, tel=%s, direc=%s where id=%s', (n,a,s,c,t,d,id))
        conn.commit()
    return redirect(url_for('crud'))

@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='Apolo', port=3306 )
    cursor = conn.cursor()
    cursor.execute('delete from registro where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crud'))

@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        Nombre = request.form['nom']
        Apellido = request.form['apellido']
        Edad = request.form['edad']
        Correo = request.form['correo']
        Telefono = request.form['tel']
        Direccion = request.form['direc']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='Apolo')
    cursor = conn.cursor()
    cursor.execute('insert into registro (nom,apellido,edad,correo,tel,direc) values (%s, %s, %s, %s, %s, %s)',(Nombre,Apellido,Edad,Correo,Telefono,Direccion))
    conn.commit()
    return redirect(url_for('crud'))

#CRUD DE PERROS

@app.route('/perros')
def perros():
    return render_template("perros.html")

@app.route('/crud2')
def crud2():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='Apolo' )
    cursor = conn.cursor()
    cursor.execute('select * from perros order by id')
    datos = cursor.fetchall()
    return render_template("crud2.html", comentario = datos)

@app.route('/edi/<string:id>')
def edi(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='Apolo', port=3306 )
    cursor = conn.cursor()
    cursor.execute('select id, nomb, raza, sexo, tam, vac, ed from perros where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editar_perros.html", dat=dato[0])

@app.route('/edi_comenta/<string:id>',methods=['POST'])
def edi_comenta(id):
    if request.method == 'POST':
        no=request.form['nomb']
        r=request.form['raza']
        sx=request.form['sexo']
        tm=request.form['tam']
        v=request.form['vac']
        e=request.form['ed']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='Apolo', port=3306 )
        cursor = conn.cursor()
        cursor.execute('update perros set nomb=%s, raza=%s, sexo=%s, tam=%s, vac=%s, ed=%s where id=%s', (no,r,sx,tm,v,e,id))
        conn.commit()
    return redirect(url_for('crud2'))

@app.route('/borr/<string:id>')
def borr(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='Apolo', port=3306 )
    cursor = conn.cursor()
    cursor.execute('delete from perros where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crud2'))

@app.route('/agr_comenta', methods=['POST'])
def agr_comenta():
    if request.method == 'POST':
        Nombr = request.form['nomb']
        Raza = request.form['raza']
        Sexo = request.form['sexo']
        Tamaño = request.form['tam']
        Vacunas = request.form['vac']
        Ed = request.form['ed']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='Apolo')
    cursor = conn.cursor()
    cursor.execute('insert into perros (nomb,raza,sexo,tam,vac,ed) values (%s, %s, %s, %s, %s, %s)',(Nombr,Raza,Sexo,Tamaño,Vacunas,Ed))
    conn.commit()
    return redirect(url_for('crud2'))

if __name__ == "__main__":
    app.run(debug=True)
