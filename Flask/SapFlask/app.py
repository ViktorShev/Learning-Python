from flask import Flask, request
from flask.helpers import url_for
from flask.templating import render_template
from flask_migrate import Migrate
from werkzeug.utils import redirect
from database import db
from models import Persona
from forms import PersonaForm

app = Flask(__name__)


# Configuracion de la DB
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'sap_flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'


# Configuracion de la app
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Inicializacion del objeto DB de SQLAlchemy
db.init_app(app)


# Configuracion de flask-migrate
migrate = Migrate()
migrate.init_app(app, db)


# Configurazion de flask-wtf
app.config['SECRET_KEY'] = 'key'


# Rutas
@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    # Listado de personas
    #personas = Persona.query.all()
    personas = Persona.query.order_by('id')
    total_personas = Persona.query.count()
    #app.logger.debug(f'Listado de personas: {personas}')
    #app.logger.debug(f'Total de personas: {total_personas}')
    return render_template('index.html', personas=personas, total_personas=total_personas)

@app.route('/detalle/<int:id>')
def ver_detalle(id):
    #persona = Persona.query.get(id)
    persona = Persona.query.get_or_404(id)
    #app.logger.debug(f'Ver persona: {persona}')
    return render_template('detalle.html', persona=persona)

@app.route('/agregar', methods=['GET', 'POST'])
def nueva_persona():
    persona = Persona()
    personaForma = PersonaForm(obj=persona)  
    if request.method == 'POST':
        if personaForma.validate_on_submit():
            personaForma.populate_obj(persona)
            # Insertamos el nuevo registro
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
            
    return render_template('nueva_persona.html', forma=personaForma)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_persona(id):
    persona = Persona.query.get_or_404(id)
    personaForma = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForma.validate_on_submit():
            personaForma.populate_obj(persona)
            #app.logger.debug(f'Persona a editar: {persona}')
            db.session.commit()
            return redirect(url_for('inicio'))

    return render_template('editar_persona.html', forma=personaForma)

@app.route('/eliminar/<int:id>')
def eliminar_persona(id):
    persona = Persona.query.get_or_404(id)
    #app.logger.debug(f'Persona a elimianar: {persona}')
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))