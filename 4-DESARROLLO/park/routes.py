from flask import Blueprint, render_template 
# Crear un Blueprint 
parq = Blueprint('parq', __name__, url_prefix='/parq')
# Definir rutas y vistas dentro del Blueprint 
@parq.route('/') 
def raiz(): 
    return 'MODULO DE PARQUEADERO'
