import numpy

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in(1,2,3,4,5,6):
                return opcion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
def arreglo_restorant():
     while True:
      arreglo_restorant = numpy.zeros((3,3))



while True:
     print(""""
          1) ver restorant
          2) Reservar mesa
          3) carta
          4) pagar
          5) cancelar
          6) salir""")
    
opcion = validar_opcion()
if opcion ==1:
   arreglo_restorant()
elif opcion ==2:
    