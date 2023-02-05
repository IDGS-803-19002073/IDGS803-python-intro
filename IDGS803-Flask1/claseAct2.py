class validador:
    cantidadCompradores=0
    tarjetaCine=""
    cantidadBoleta=0



    def validarCantidadMaximaBoletos(self,cantidadCompradores,cantidadBoleta):
        self.cantidadBoleta= cantidadBoleta
        self.cantidadCompradores= cantidadCompradores
        cantidadMaxima=self.cantidadCompradores*7
        if(self.cantidadBoleta>cantidadMaxima):
            return "maxima"

    def validarTarjetaCine(self,tarjetaCine):
        self.tarjetaCine=tarjetaCine
        if(self.tarjetaCine=="si"):
            return True
        if(self.tarjetaCine=="no"):
            return False

    def calcularDescuentoConTarjeta(self,cantidadBoleta):
        self.cantidadBoleta= cantidadBoleta
        valorTotal= self.cantidadBoleta*12

        if self.cantidadBoleta >5:
                descuento= valorTotal-(valorTotal*0.15)
                descuentoFinal= descuento-(descuento * 0.10)
                return descuentoFinal

        elif self.cantidadBoleta ==3 or self.cantidadBoleta ==4 or self.cantidadBoleta ==5 :
                descuento= valorTotal-(valorTotal*0.10)
                descuentoFinal= descuento-(descuento * 0.10)
                return descuentoFinal
        elif self.cantidadBoleta <=2 :
                descuentoFinal= valorTotal-(valorTotal * 0.10)
                return descuentoFinal

    def calcularDescuentoSinTarjeta(self,cantidadBoleta):
        self.cantidadBoleta= cantidadBoleta
        valorTotal= self.cantidadBoleta*12

        if self.cantidadBoleta >5:
                descuento= valorTotal-(valorTotal*0.15)
                return descuento
        elif self.cantidadBoleta ==3 or self.cantidadBoleta ==4 or self.cantidadBoleta ==5 :
                descuento= valorTotal-(valorTotal*0.10)
                return descuento
        elif self.cantidadBoleta <=2 :
                return valorTotal
        
    
        