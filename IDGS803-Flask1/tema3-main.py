from flask import Flask

#instancia al nombre del proyecto , despues levantamos el servidor
app= Flask(__name__)

#todo decorador lleva associado un metodo y un return
@app.route("/user/<string:user>")
def user(user):
    return "Hola mundo "+user

@app.route("/numero/<int:numero>")
def numero(numero):
    return "Tengo {} años".format(numero)

@app.route("/user/<int:id>/<string:name>")
def func(id,name):
    return "ID: {} Nombre: {}".format(id,name)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma es {}".format(n1+n2)

if __name__=="__main__":
    app.run(debug=True)