class operasbas():
    #definir propiedades de clase
    num1=0
    num2=0
    res=0
    
    #definir constructor de la clase   
    def sumar(self,a,b):
        self.num1=a
        self.num2=b
        self.res=self.num1+self.num2
        return self.res

    def restar(self,a,b):
        self.num1=a
        self.num2=b
        self.res=self.num1-self.num2
        return self.res

    def multiplicar(self,a,b):
        self.num1=a
        self.num2=b
        self.res=self.num1*self.num2
        return self.res

    def dividir(self,a,b):
        self.num1=a
        self.num2=b
        self.res=self.num1/self.num2
        return self.res

def main():
    obj=operasbas()
     
    while True: 
      print("Menu OPCION sumar=1 , restar=2 , multiplicar=3 , dividir=4 , salir=5") 
      num1=int(input("Escoger: ")) 
      if num1 == 1:
            numero1=int(input("dame numero 1: "))
            numero2=int(input("dame numero 2: "))
            print("{} + {} = {}".format(numero1, numero2, obj.sumar(numero1,numero2)))
            
      elif num1 == 2:
            numero1=int(input("dame numero 1: "))
            numero2=int(input("dame numero 2: "))
            print("{} - {} = {}".format(numero1, numero2, obj.restar(numero1,numero2)))
            
      elif num1 == 3:
            numero1=int(input("dame numero 1: "))
            numero2=int(input("dame numero 2: "))
            print("{} * {} = {}".format(numero1, numero2, obj.multiplicar(numero1,numero2)))
            
      elif num1 == 4:
            numero1=int(input("dame numero 1: "))
            numero2=int(input("dame numero 2: "))
            print("{} / {} = {}".format(numero1, numero2, obj.dividir(numero1,numero2)))
            
        
      elif num1 == 5:
            return "adios"
            
            

if __name__=='__main__':
    main()
        