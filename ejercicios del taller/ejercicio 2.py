import math

# Clase Punto que representa un punto en el plano cartesiano
class Punto:
    def __init__(self, x, y):
        self.x: float = x
        self.y: float = y

    # Método para mostrar las coordenadas del punto
    def mostrar(self):
        print(f"Coordenadas: ({self.x}, {self.y})")

    # Método para cambiar las coordenadas del punto
    def mover(self, newx, newy):
        self.x = newx
        self.y = newy

    # Método para calcular la distancia entre dos puntos
    def calcular_distancia(self, otro_punto):
        diferencia_x = otro_punto.x - self.x
        diferencia_y = otro_punto.y - self.y
        distancia = math.sqrt(diferencia_x**2 + diferencia_y**2)
        return distancia

# Crear una instancia de la clase Punto
punto1 = Punto(3, 4)

# Mostrar las coordenadas originales del punto
punto1.mostrar()

# Mover el punto a nuevas coordenadas
punto1.mover(7, 8)

# Mostrar las coordenadas después de moverlo
punto1.mostrar()

# Crear otra instancia de la clase Punto
punto2 = Punto(1, 1)

# Calcular y mostrar la distancia entre los dos puntos
distancia_entre_puntos = punto1.calcular_distancia(punto2)
print(f"La distancia entre los puntos es: {distancia_entre_puntos}")





