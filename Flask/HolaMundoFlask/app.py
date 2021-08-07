from flask import Flask, request, render_template, session
from flask.helpers import url_for
from flask.json import jsonify
from werkzeug.exceptions import abort
from werkzeug.utils import redirect


app = Flask(__name__)

app.secret_key = 'key'

#http://localhost:5000/
@app.route('/')
def inicio():
    if 'username' in session:
        return render_template('inicio.html', user=session['username']) 
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Omitimos validacion del usuario y su contraseña
        # Agregar el usuario a la sesion
        session['username'] = request.form['username']
        return redirect(url_for('inicio'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre}'

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es: {edad}'

@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)

@app.route('/redir')
def redir():
    return redirect(url_for('mostrar_nombre', nombre='Juan'))

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina404(error):
    return render_template('error404.html', error=error), 404

#REST = Representational state transfer

@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_json(nombre):
    valores = {
        'nombre': nombre,
        'metodo_http': request.method
    }
    return jsonify(valores)