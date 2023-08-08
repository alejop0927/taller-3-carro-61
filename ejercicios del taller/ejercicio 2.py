# Cree una clase Punto que represente un punto en el plano cartesiano.
class Punto:
    def __init__(self, x, y):
        self.x: float = x
        self.y: float = y




#A la clase del punto anterior, defínale los siguientes métodos:
#- Un método mostrar que imprima por consola las coordenadas del punto


    def mostrar(self):
        print(f"Coordenadas:({self.x}, {self.y})")


#- Un método mover que cambie las coordenadas del punto

    def mover(self,newx,newy):
        self.x=newx
        self.y=newy




#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.

     def calcular(self,operaion):

operacionx =x-newx
operaciony =y-newy
       print(operacion)



         punto1 = Punto(3, 4)

         punto1.mostrar()

         punto1.mover(7, 8)

         punto1.mostrar()





