from flask import Flask , render_template

from flask_cors import CORS
from admin.routes import admin 
from park.routes import parq
from piscina.routes import pisc
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
    return render_template("menu.html")
if __name__=='__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
