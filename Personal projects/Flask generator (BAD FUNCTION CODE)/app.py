from flask import Flask
from flask.templating import render_template
from functions.random_apex import random_weapons, random_legends


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate/<type>')
def generate(type):
    if type == 'squad':
        legend1, legend2, legend3 = random_legends()
        gun1, gun2 = random_weapons()
        gun3, gun4 = random_weapons()
        gun5, gun6 = random_weapons()
        return render_template(
        'generate_squad.html', 
        legend1=legend1, 
        legend2=legend2, 
        legend3=legend3, 
        gun1=gun1, 
        gun2=gun2, 
        gun3=gun3, 
        gun4=gun4, 
        gun5=gun5, 
        gun6=gun6
        )
    elif type == 'solo':
        legend1, legend2, legend3 = random_legends()
        gun1, gun2 = random_weapons()
        return render_template('generate_solo.html', legend=legend1, gun1=gun1, gun2=gun2) 


