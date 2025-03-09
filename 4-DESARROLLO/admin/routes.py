from flask import Blueprint, render_template 
import pandas as pd
# Crear un Blueprint 
admin = Blueprint('admin', __name__, url_prefix='/admin')
# Definir rutas y vistas dentro del Blueprint 
@admin.route('/') 
def raiz(): 
    menu = []
    a = pd.read_csv('admin/menu.csv')

    # Convert all rows to a list of lists (faster approach)
    menu = a.values.tolist()

    return render_template('menu.html',menus=menu)