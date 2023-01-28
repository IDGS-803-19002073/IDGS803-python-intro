from flask import Flask, render_template

#instancia al nombre del proyecto , despues levantamos el servidor
app= Flask(__name__)

#todo decorador lleva associado un metodo y un return
@app.route("/")
def index():
    nombre = "Jorge"
    lista1=["Español","Ingles","Quimica"]
    return render_template("index.html",nombre=nombre,lista1=lista1)


@app.route("/usuarios")
def usuarios():
    return render_template("archivo2.html")

if __name__=="__main__":
    app.run(debug=True)