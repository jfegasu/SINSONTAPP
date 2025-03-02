from flask import Blueprint, render_template 
# Crear un Blueprint 
pisc = Blueprint('pisc', __name__, url_prefix='/pisc')
# Definir rutas y vistas dentro del Blueprint 
@pisc.route('/') 
def raiz(): 
    return 'MODULO DE PISCINA'