from flask import Blueprint, render_template 
# Crear un Blueprint 
admin = Blueprint('admin', __name__, url_prefix='/admin')
# Definir rutas y vistas dentro del Blueprint 
@admin.route('/') 
def raiz(): 
    return 'MODULO DE ADMINISTRACION'