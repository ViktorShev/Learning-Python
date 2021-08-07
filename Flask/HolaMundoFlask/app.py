from flask import Flask, request, render_template
from flask.helpers import url_for
from werkzeug.utils import redirect


app = Flask(__name__)

#http://localhost:5000/

@app.route('/')
def inicio():
    app.logger.info(f'Entering the path: {request.path}')                
    return 'Hola Mundo desde Flask.'

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