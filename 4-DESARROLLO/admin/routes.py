from flask import Blueprint, render_template 
import pandas as pd
from utils.Utilitarios import CargaMenu,getRol,valideUsuario,crearTabla,Ejecutar
# Crear un Blueprint 
admin = Blueprint('admin', __name__, url_prefix='/admin')
# Definir rutas y vistas dentro del Blueprint 
@admin.route('/') 
def raiz(): 
    # return "ADMIN"
    
    vcol=['UNIDAD','APARTAMENTOS X UNIDAD']
    # aa=crearTabla('usuario',col,{"login":"'prueba'"})
    aux=1
    sql=f"SELECT IDUNIDAD,NOMUNIDAD,(SELECT COUNT(*) FROM APARTAMENTO WHERE IDUNIDAD=U.IDUNIDAD) APTO FROM UNIDAD U"
    print(sql)
    aa=Ejecutar(sql)
    confi=[{
            "icono":"spoke",
            "titu":"Editar",
            "key":0
            },
            {
            "icono":"delete",
            "titu":"Borrar",
            "key":1
            },
            {
            "icono":"hotel",
            "titu":"Apartamentos",
            "key":1
            }
            ]
    
    # aa=crearTabla('usuario',['rol'],None)

    return render_template('admin_tabla.html',aa=aa,vcol=vcol,i=len(vcol),despla=1,key=0,nivel=0,confi=confi)