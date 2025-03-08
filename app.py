from flask import Flask , render_template
import pandas as pd

from flask_cors import CORS
from admin import admin 
# from park.routes import parq
# from piscina.routes import pisc
# importar el Blueprint 
# Crear la aplicación Flask 
app = Flask(__name__) 

# Registrar el Blueprint en la aplicación 
app.register_blueprint(admin)
app.register_blueprint(parq)
app.register_blueprint(pisc)
@app.route("/")
def raiz():
    return render_template("index.html")
@app.route("/banner")
def banner():
    return render_template("banner.html")
@app.route("/menu")
def menu():
    menus=pd.read_csv("menu.csv",header=True)
    return render_template("menu.html")
@app.route("/footer")
def footer():
    return render_template("footer.html")
if __name__=='__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
