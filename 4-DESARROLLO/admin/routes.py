from flask import Blueprint, render_template 
import pandas as pd
from utils.Utilitarios import CargaMenu,getRol,valideUsuario,crearTabla,Ejecutar
# Crear un Blueprint 
admin = Blueprint('admin', __name__, url_prefix='/admin')
# Definir rutas y vistas dentro del Blueprint 
@admin.route('/') 
def raiz(): 
    # return "ADMIN"
    col=['rol']
    vcol=['ROL']
    # aa=crearTabla('usuario',col,{"login":"'prueba'"})
    aux=1
    sql=f"select * from apartamento where idapto=%d" % aux
    print(sql)
    aa=Ejecutar(sql)
    
    # aa=crearTabla('usuario',['rol'],None)
    return render_template('admin_tabla.html',aa=aa,vcol=vcol)