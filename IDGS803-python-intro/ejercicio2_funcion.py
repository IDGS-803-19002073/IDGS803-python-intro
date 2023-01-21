
def sumar():
    
    resultado = num1 + num2
    print("{} + {} = {}".format(num1, num2, resultado))

def restar():
    num1=int(input("dame numero 1: "))
    num2=int(input("dame numero 2: "))
    resultado = num1- num2
    print("{} - {} = {}".format(num1, num2, resultado))

def multiplicar():
    num1=int(input("dame numero 1: "))
    num2=int(input("dame numero 2: "))
    resultado = num1* num2
    print("{} * {} = {}".format(num1, num2, resultado))

def dividir():
    num1=int(input("dame numero 1: "))
    num2=int(input("dame numero 2: "))
    resultado = num1/num2
    print("{} / {} = {}".format(num1, num2, resultado))

def main():
    print("Menu OPCION sumar=1 , restar=2 , multiplicar=3 , dividir=4 , salir=5")
    num1=int(input("Escoger: "))  
    while num1!=5:
      if num1 == 1:
        return sumar()
      elif num1 == 2:
        return restar()
      elif num1 == 3:
        return multiplicar()
      elif num1 == 4:
        return dividir()
      elif num1 == 5:
        return "adios"

if __name__ == '__main__':
    main()
    
      


