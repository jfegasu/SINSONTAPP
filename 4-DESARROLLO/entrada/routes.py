from flask import Blueprint, render_template 
# Crear un Blueprint 
entra = Blueprint('entra', __name__, url_prefix='/entra')
# Definir rutas y vistas dentro del Blueprint 
@entra.route('/') 
def raiz(): 
    return 'MODULO DE INGRESO PEATONAL'
