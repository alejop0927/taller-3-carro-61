#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.
class Carro:
   def __init__(self,velocidad_maxima,kilometraje):
      self.velocidad_maxima: int = velocidad_maxima
      self.kilometraje: float = kilometraje

a=Carro(75,80)
print(a.velocidad_maxima,a.kilometraje)

