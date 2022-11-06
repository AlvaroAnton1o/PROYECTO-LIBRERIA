from flask import render_template, Flask, url_for, redirect, request
import dbMongo

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/inicio')
def inicio():
    return redirect('/')

@app.route('/agregarLibro')
def agregarLibro():
    return render_template('pages/agregar.html')


@app.route('/guardarLibro', methods=['GET', 'POST'])
def guardarLibro():
    codigo = request.form['txtCodigo']
    nombre = request.form['txtNombre']
    categoria = request.form['txtCategoria']
    autor = request.form['txtAutor']
    data = {'codigo':codigo, 'nombre':nombre, 'categoria':categoria, 'autor':autor}
    dbMongo.connection('Libreria','Libros')
    dbMongo.saveProducto(data)
    return redirect('agregarLibro')

if __name__=='__main__':
    app.run(debug=True)

