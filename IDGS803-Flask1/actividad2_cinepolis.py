import claseAct2 as objValidador
from flask import Flask, render_template,request,flash
app= Flask(__name__) 


#Rutas de paginas
@app.route("/cinepolis")
def cinepolis():
    return render_template("cinepolis.html") 

@app.route("/validacion", methods=["POST"])
def resultado():
    cantidad= request.form.get("txtCantidad")
    cantidadCompradores= request.form.get("txtCantidadCompradores")
    op=request.form.get("op")
    intCantidadBoletas= int(cantidad)
    intCantidadCompradores= int(cantidadCompradores)

    obj=objValidador.validador()
     
    if obj.validarCantidadMaximaBoletos(intCantidadCompradores,intCantidadBoletas)=="maxima":  
        return render_template("cinepolis.html",mensaje="Cantidad de boletos a comprar excedida")
    else:
        if obj.validarTarjetaCine(op):
            return render_template("cinepolis.html", resultado=obj.calcularDescuentoConTarjeta(intCantidadBoletas)) 
        else:
            return render_template("cinepolis.html", resultado=obj.calcularDescuentoSinTarjeta(intCantidadBoletas))
          
if __name__=="__main__":
    app.run( debug=True) #debug=True para que se actualice automaticamente