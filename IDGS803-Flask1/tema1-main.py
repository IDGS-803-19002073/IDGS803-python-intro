from flask import Flask

#instancia al nombre del proyecto , despues levantamos el servidor
app= Flask(__name__)

#todo decorador lleva associado un metodo y un return
@app.route("/")
def index():
    return "Hola mundo"

if __name__=="__main__":
    app.run(debug=True)